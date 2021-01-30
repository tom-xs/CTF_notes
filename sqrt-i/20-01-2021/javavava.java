import java.lang.reflect.Array;

public class javavava {
    public static void main(String[] args) {
        String flag = "ictf{REDACTEDFLAG}";
        char[] flagVars = new char[flag.length()];
        for (int i = 0; i < flag.length(); i++) {
            flagVars[i] = flag.charAt(i);
        }
        char[] flagVarsBirds = new char[flagVars.length];
        int[] coolFinal = new int[flagVars.length];
        int count = 0;
        for (char c: flagVars) {
            int a = c;
            int ind = new String(flagVars).indexOf(c);
            if (c != flagVars.length - 1) {
                for (int i = 0; i < flag.length(); i++) {
                    char d = (char) ((ind ^ 15) + (2 * a));
                    flagVarsBirds[i] = d;
                }
            } else {
                System.out.println("that shouldn't have happened D:");
            }
            int fire = flagVarsBirds[0];
            boolean ILikeRev = false;
            for (int i = 0; i < flagVarsBirds.length; i++) {
                if (fire == flagVarsBirds[i] && !ILikeRev) {
                    ILikeRev = true;
                } else if (fire != flagVarsBirds[i]) {
                    System.out.print(" " + fire);
                    fire = flagVarsBirds[i];
                    ILikeRev = false;
                }
            }
            coolFinal[count] = fire;
            count++;
        }
        for (int i = 0; i < flagVarsBirds.length; i++) {
            System.out.print(coolFinal[i] + " ");
        }

        // 225 212 245 216 257 222 139 244 139 196 225 76 196 212 97 97 247 280 
        decode();

    }

    /*
     * meu código
    */
    public static String decode(){
        String arr[] = "225 212 245 216 257 222 139 244 139 196 225 76 196 212 97 97 247 280".split(" ");
        //String arr[] = "225 212 245 216 257 174 147 144 137 140 173 147 144 142 153 137 173 280".split(" ");
        String r = "";
        String rchar = "";
        for(String c:arr){
            int d = Integer.parseInt(c);
            
            int ind = indOf(arr, c);
            
            int x = ind^15;
            int a = (d-x)/2;
            r+=a+" ";
            rchar+=(char)a;

        }
        System.out.println();
        System.out.println(r);
        System.out.println(rchar);

        return "";
    } 
    public static int indOf(String[] arr,String s){
        int c = 0;

        for(String i:arr){
            if(i.equals(s)){
                return c;
            }else{
                c++;
            }
        }
        return 0;
    }
}
