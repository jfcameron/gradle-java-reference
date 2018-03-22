// 
// 
// 

import java.nio.file.Path;
import java.nio.file.Paths;

/**
 * Program entry object
 */
public class App
{
    /**
     * Example func
     */
    public String getGreeting()
    {
        return "Hello world.";
    }

    /**
     * Main entry
     */
    public static void main(String[] args)
    {
        System.out.println(new App().getGreeting());

        Path currentRelativePath = Paths.get("");
        String s = currentRelativePath.toAbsolutePath().toString();
        System.out.println("Current relative path is: " + s);

        //String path = App.getBasePathForClass(App.class);
        //String applicationPath=  new File(path + "application.jar").getAbsolutePath();

        //System.out.println(path);
    }
}
