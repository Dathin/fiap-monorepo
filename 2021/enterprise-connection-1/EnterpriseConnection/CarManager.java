package EnterpriseConnection;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Map;
import java.util.Calendar;
import java.util.Date;
import java.util.HashMap;

public class CarManager {
  final int ITERATION_MINUTES = 5;

  Date currentTime;
  Date endOfCycle;
  Date maintenanceStart;
  Map<Integer, Line> lines;  
  SimpleDateFormat dateFormatter = new SimpleDateFormat("yyyy-mm-dd hh:mm:ss");
  
  public CarManager(Map<Integer, Line> lines) throws ParseException {
    this.currentTime = dateFormatter.parse("2021-04-18 04:40:00");
    this.endOfCycle = this.addTime(this.currentTime, Calendar.HOUR, 24);
    this.maintenanceStart = this.addTime(this.currentTime, Calendar.MINUTE, 1159);
    
    this.lines = lines;
  }

  private Date addTime(Date date, int unit, int amountOfUnits) {
    Calendar calendar = Calendar.getInstance();
    calendar.setTime(date);
    calendar.add(unit, amountOfUnits);
    return calendar.getTime();
  }

  private void printTime(Date date) {
    Calendar calendar = Calendar.getInstance();
    calendar.setTime(date);
    System.out.printf("[%d:%d]\n", calendar.get(Calendar.HOUR_OF_DAY), calendar.get(Calendar.MINUTE));
  }

  private boolean isMaintenanceTime() {
    return currentTime.compareTo(maintenanceStart) > 0;
  }

  private boolean canSendMaintenanceCar(Line line) {
    int minutesUntilDone = line.stations.length * ITERATION_MINUTES * 2;
    Date maintenanceRunEnd = this.addTime(currentTime, Calendar.MINUTE, minutesUntilDone);

    return maintenanceRunEnd.compareTo(endOfCycle) < 0;
  }

  public void start() {
    while(currentTime.compareTo(endOfCycle) != 0) {
      printTime(currentTime);

      for (int i = 0; i < lines.size(); i++) {
        Line line = lines.get(i);

        if (isMaintenanceTime()) {
          line.nextWithMaintenance(canSendMaintenanceCar(line));
        } else {
          line.next();  
        }
      }

      this.currentTime = this.addTime(currentTime, Calendar.MINUTE, ITERATION_MINUTES);
    }

    System.out.println("Fim da execução");
  }
}
