package EnterpriseConnection;

import java.util.List;
import java.util.ArrayList;

public class Line {
  String name;
  List<Car> carDepot;
  Station[] stations;
  Boolean addCarOnNext = true;

  public Line(String name, int numberOfStations) {
    this.name = name;
    carDepot = new ArrayList<Car>();
    stations = new Station[numberOfStations];
    for (int i = 0; i < numberOfStations; i++) {
      stations[i] = new Station(i);
    }
  }

  public void addCarsToDepot(List<Car> cars) {
    carDepot.addAll(cars);
  }

  private Car getCarFromDepot(CarType type) {
    for (int i = 0; i < carDepot.size(); i++) {
      Car car = carDepot.get(i);
      if (car.type == type) {
        carDepot.remove(i);
        return car;
      }
    }

    return null;
  }

  private void printLineStatus() {
    for (int i = 0; i < stations.length; i++) {
      Station station = stations[i];
      if (station.hasCar(Direction.RIGHT) && station.hasCar(Direction.LEFT)) {
        Car carGoingRight = station.getCar(Direction.RIGHT);
        Car carGoingLeft = station.getCar(Direction.LEFT);
        System.out.printf("[Linha %s - Estação %d]: %s indo e %s voltando\n", name, station.number, carGoingRight,
            carGoingLeft);
      } else if (station.hasCar(Direction.RIGHT)) {
        Car car = station.getCar(Direction.RIGHT);
        System.out.printf("[Linha %s - Estação %d]: %s indo\n", name, station.number, car);
      } else if (station.hasCar(Direction.LEFT)) {
        Car car = station.getCar(Direction.LEFT);
        System.out.printf("[Linha %s - Estação %d]: %s voltando\n", name, station.number, car);
      }
    }
  }

  private void nextRight() {
    for (int i = stations.length - 1; i >= 0; i--) {
      boolean isLastStation = i == stations.length - 1;
      Station currentStation = stations[i];

      if (isLastStation) {
        if (currentStation.hasCar(Direction.LEFT)) {
          Station previousStation = stations[i - 1];
          Car car = currentStation.removeCar(Direction.LEFT);
          previousStation.addCar(Direction.LEFT, car);
        }

        if (currentStation.hasCar(Direction.RIGHT)) {
          Car car = currentStation.removeCar(Direction.RIGHT);
          currentStation.addCar(Direction.LEFT, car);
        }
      } else {
        Station nextStation = stations[i + 1];
        if (currentStation.hasCar(Direction.RIGHT)) {
          Car car1 = currentStation.removeCar(Direction.RIGHT);
          nextStation.addCar(Direction.RIGHT, car1);
        }
      }
    }
  }

  private void nextLeft(boolean isMaintenance) {
    for (int i = 0; i < stations.length; i++) {
      boolean isFirstStation = i == 0;
      Station currentStation = stations[i];

      if (isFirstStation) {
        if (currentStation.hasCar(Direction.LEFT) && isMaintenance) {
          Car car = currentStation.removeCar(Direction.LEFT);
          carDepot.add(car);
          System.out.printf("%s retornou para o pátio\n", car);
        }

        if (currentStation.hasCar(Direction.LEFT) && !currentStation.hasCar(Direction.RIGHT)) {
          Car car = currentStation.removeCar(Direction.LEFT);
          currentStation.addCar(Direction.RIGHT, car);
        }

        if (currentStation.hasCar(Direction.RIGHT)) {
          Station nextStation = stations[i + 1];
          Car car1 = currentStation.removeCar(Direction.RIGHT);
          nextStation.addCar(Direction.RIGHT, car1);
        }
      } else {
        Station previousStation = stations[i - 1];
        if (currentStation.hasCar(Direction.LEFT)) {
          Car car2 = currentStation.removeCar(Direction.LEFT);
          previousStation.addCar(Direction.LEFT, car2);
        }
      }
    }
  }

  public boolean trySendMaintenanceCar() {
    if (addCarOnNext && !stations[0].hasCar(Direction.RIGHT)) {
      Car car = getCarFromDepot(CarType.MAINTENANCE);
      if (car != null) {
        stations[0].addCar(Direction.RIGHT, car);
        this.addCarOnNext = false;
        printLineStatus();
        return true;
      }
    }

    return false;
  }

  public boolean nextWithMaintenance(boolean canSendMaintenanceCar) {
    this.nextLeft(true);
    this.nextRight();
    boolean sent = false;

    if (addCarOnNext && !stations[0].hasCar(Direction.RIGHT) && canSendMaintenanceCar) {
      Car car = getCarFromDepot(CarType.MAINTENANCE);
      if (car != null) {
        stations[0].addCar(Direction.RIGHT, car);
        this.addCarOnNext = false;
        sent = true;
      }
    } else {
      this.addCarOnNext = true;
    }

    printLineStatus();
    return sent;
  }

  public void next() {
    this.nextLeft(false);
    this.nextRight();

    if (addCarOnNext && !stations[0].hasCar(Direction.RIGHT)) {
      Car car = getCarFromDepot(CarType.PASSENGER);
      if (car != null) {
        stations[0].addCar(Direction.RIGHT, car);
        this.addCarOnNext = false;
      }
    } else {
      this.addCarOnNext = true;
    }

    printLineStatus();
  }
}