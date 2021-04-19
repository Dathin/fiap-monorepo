package EnterpriseConnection;

import java.util.HashMap;
import java.util.Map;

public class Station {
  int number;
  Map<Direction, Car> cars;

  public Station(int number) {
    this.number = number;
    cars = new HashMap<Direction, Car>();
  }

  public boolean hasCar(Direction direction) {
    Car car = cars.get(direction);
    if (car == null) {
      return false;
    }

    return true;
  }

  public Car getCar(Direction direction) {
    return cars.get(direction);
  }

  public void addCar(Direction direction, Car car) {
    if (car == null) {
      throw new RuntimeException(String.format("Cannot add null car to station %s", number));
    }

    if (hasCar(direction)) {
      Car x = cars.get(direction);
      throw new RuntimeException(String.format("%s and %s crashed", car, x));
    }

    cars.put(direction, car);
  }

  public Car removeCar(Direction direction) {
    Car car = cars.get(direction);
    if (car == null) {

    }
    cars.remove(direction);
    return car;
  }
}
