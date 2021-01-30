public class javavava {
    public static void main(String[] args) {
        String flag = "ictf{REDACTEDFLAG}";
        char[] flagVars = new char[flag.length()];
        for (int i = 0; i < flag.length(); i++) {
            flagVars[i] = flag.charAt(i);
        }
        char[] flagVarsBirds = new char[flagVars.length];
        int[] coolFinal = new int[flagVars.length];

        int[] a_arr = new int[flagVars.length];
        int[] i_arr = new int[flagVars.length];

        int count = 0;
        for (char c: flagVars) {
            int a = c;
            int ind = new String(flagVars).indexOf(c);
            //System.out.println("count = "+count+"\nind = "+ind+"\ncoolFinal"+printArr(coolFinal));
            if (c != flagVars.length - 1) {
                for (int i = 0; i < flag.length(); i++) {
                    char d = (char)((ind ^ 15) + (2 * a));
                    flagVarsBirds[i] = d;

                    a_arr[count] = a;
                    i_arr[count] = ind;

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
                    System.out.print(" "+fire);
                    fire = flagVarsBirds[i];
                    ILikeRev = false;
                }
            }
            coolFinal[count] = fire;
            count++;
        }
        System.out.println();
        for (int i = 0; i < flagVarsBirds.length; i++) {
            System.out.print((coolFinal[i]) + " ");
        }
        System.out.println("");
        System.out.println(printArr(a_arr));
        System.out.println(printArr(i_arr));
        // 225 212 245 216 257 222 139 244 139 196 225 76 196 212 97 97 247 280 
    }

public static String printArr(int[] arr){
    String s = new String("[");
    for (int i : arr) {
        s = s + i +",";
    }
    s = s+"]";
    return s;
}
public static String reverse(int[] arr){
    String s = new String("");

    return s;
}
}