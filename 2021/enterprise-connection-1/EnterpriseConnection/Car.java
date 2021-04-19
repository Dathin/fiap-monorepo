package EnterpriseConnection;

public class Car {
  String name;
  CarType type;

  public Car(String name, CarType type) {
    this.name = name;
    this.type = type;
  }

  public String toString() {
    return String.format("Carro %s", name);
  }
}
