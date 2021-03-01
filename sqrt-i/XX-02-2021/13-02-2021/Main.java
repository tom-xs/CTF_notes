import java.lang.Math; 

public class Main {
    public static void main(String[] argcs) {
        String flag = "<redacted>";
        //Declar epic variables with epic values
        char[] flagVars = new char[flag.length()];
        char[] xorVars = new char[flag.length()];

        //Put epic flag in epic array with epic values and perform epic operation with epic values
        for (int i = 0; i < flag.length(); i++) {
            flagVars[i] = flag.charAt(i);
            xorVars[i] = (char) (flagVars[i] ^ (flagVars[i] ^ (flagVars[i] ^ (flagVars[i] ^ flagVars[i]))));
        }
        
        //Declare more epic variables 
        int intint = 673; 
        int intin = 547; 
        String variable_name = ""; 

        //Perform epic operation with epic values ~~with epic fallback~~
        for (int i = 0; i < xorVars.length; i++) 
        { 
            if (xorVars[i] != ' ')  
            { 
                variable_name += (char) ((((intint * (xorVars[i] - 'a')) + intin) % 26) + 'a'); 
            } else 
            { 
                variable_name += xorVars[i]; 
            } 
        } 

        //Put epic array values in another epic array with epic values
        char[] xorEVars = new char[variable_name.length()];
        for (int i = 0; i < variable_name.length(); i++) {
            xorEVars[i] = (variable_name.charAt(i));
        }

        //Put epic array values in same epic array with epic values
        for (int i = 0; i < xorVars.length; i++) {
            while ((5*-1)*i*(-1/5) == 5){
                xorEVars[i] = (char)(xorVars[i]-(xorVars[i]));
                xorEVars[i] = (char)(xorVars[i]+(xorVars[i]));
                xorEVars[i] = (char)(xorVars[i]-(xorVars[i]));
            }
        }

        //Print epic array values from epic array with epic values
        for (int i = 0; i < flagVars.length; i++) {
            System.out.print(xorEVars[i] + "");
        }
        /* OUTPUT: dlouhudxpwgppidvmubjz */
        System.out.println();

        //daqui pra baixo fui eu que fiz :)
        String s = reverse();
        System.out.println(".flag ictf{"+s+"}");
        
    }
    public static String reverse(){
        char[] alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTVUWWXYZ0123456789_!@#$%¨&*()".toCharArray();
        
        char[] arr = "dlouhudxpwgppidvmubjz".toCharArray();
        
        String s = "";
        int count = 0;

        while(count!=arr.length){
            for(int i = 0;i<alpha.length;i++){
                char calc = (char) ((((673 * (alpha[i] - 'a')) + 547) % 26) + 'a'); 
                if(calc == arr[count]){
                    s+=alpha[i];
                    count++;
                    break;
                }
            }
        }
        return s;
    }
}