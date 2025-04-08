import java.util.*;

public class TestCalendar {
    public static void main(String[] args) {
        Calendar calendar = new GregorianCalendar();

        System.out.println("Current time is " + new Date());

        System.out.println("Year:\t" + calendar.get(Calendar.YEAR));
        System.out.println("Month:\t" + calendar.get(Calendar.MONTH));
        System.out.println("Date:\t" + calendar.get(Calendar.DATE));
        System.out.println("Hour:\t" + calendar.get(Calendar.HOUR));

        System.out.println("Minute:\t" + calendar.get(Calendar.MINUTE));


        Calendar calendar1 = new GregorianCalendar(2001,8,11);

    }

    public static String dayNameOfWeek(int dayOfWeek) {
        switch(dayOfWeek) {
            case 1: return "Sunday";
            case 2: return "Monday";
            case 3: return "Tuesday";
            case 4: return "Wednesday";
            case 5: return "Thursday";
            case 6: return "Friday";
            case 7: return "Saturday";
            default: return null;
        }
    }
}