import java.text.ParseException;
import java.util.*;

import EnterpriseConnection.*;

public class Main {
  
  public static int generateRandomNumber(int high, int low) {
    Random r = new Random();
    return r.nextInt(high - low) + low;
  }

  public static List<Car> getCars(int n, CarType type) {
    
    List<Car> cars = new ArrayList<Car>();

    for (int i = 0; i < n; i++) {
      String carName = Integer.toString(generateRandomNumber(10000, 1000));
      Car car = type == CarType.PASSENGER 
        ? new PassengerCar(carName) 
        : new MaintenanceCar(carName);

      cars.add(car);
    }

    return cars;
  }
  
  public static void main(String[] args) {
    Line line7 = new Line("Brás - Jundiaí", 19);
    line7.addCarsToDepot(getCars(22, CarType.PASSENGER));
    line7.addCarsToDepot(getCars(3, CarType.MAINTENANCE));

    Line line10 = new Line("Julio Prestes - Itapevi", 24);
    line10.addCarsToDepot(getCars(19, CarType.PASSENGER));
    line10.addCarsToDepot(getCars(2, CarType.MAINTENANCE));
    
    Line line12 = new Line("Calmon Viana", 16);
    line12.addCarsToDepot(getCars(19, CarType.PASSENGER));
    line12.addCarsToDepot(getCars(4, CarType.MAINTENANCE));

    Map<Integer, Line> lines = new HashMap<Integer, Line>();
    lines.put(0, line7);
    lines.put(1, line10);
    lines.put(0, line12);

    try {
      new CarManager(lines).start();

    } catch (ParseException err) {
      System.out.println("Um erro inesperado ocorreu");
    }
  }  
}
