import java.net.http.HttpResponse;
import java.util.Scanner;

public class SimpleWeatherRetriever {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter latitude: ");
        String latitude = scanner.nextLine();

        System.out.print("Enter longitude: ");
        String longitude = scanner.nextLine();

        String entireUrl = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m&temperature_unit=fahrenheit&wind_speed_unit=mph&precipitation_unit=inch&timezone=America%2FNew_York";

        // Build the API URL
        String apiUrl = "https://api.open-meteo.com/v1/forecast?latitude=" + latitude
                + "&longitude=" + longitude
                + "&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m";




        scanner.close();
    }
}
