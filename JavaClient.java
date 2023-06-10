import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.net.Socket;
import java.util.Scanner;
public class JavaClient {
    public static void main(String[] args) {
        Socket s=null;
        DataInputStream in=null;
        DataOutputStream out=null;
        try{
           Scanner sin=new Scanner(System.in);         
           while(true){
            s=new Socket("bala",1234);
            in=new DataInputStream(s.getInputStream());
            out=new DataOutputStream(s.getOutputStream());
            System.out.print(">>>");
            String sendData=sin.nextLine();
            out.write(sendData.getBytes());
            if(sendData.equals("exit()") || sendData.equals("quit()") ) 
                System.exit(0);
            else{
               byte[] bdata=new byte[4096];
               String sdata=String.valueOf(in.read(bdata,0,bdata.length)); //numbers
               String edata = new String(bdata);                           //text
               if(edata.trim().equals(""))
                   System.out.println(sdata); // number data
               else{
                    System.out.println(edata.trim()); //text data
                    if(edata.contains("Runtime Error: ")) {
                        System.out.println("Connection Terminated, reconnect again..");
                        System.exit(0);                                    }
                     }
                }
           }
        }catch(Exception e){  System.out.println("Error " + e);  }
    }
} 
