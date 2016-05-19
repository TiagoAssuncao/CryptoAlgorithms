import java.util.Scanner;


public class Aes {
	
    public static String [][] m = new String[4][4];
    public static String [][] k = new String[4][4];
    public static String[][] subKeys = new String[4][4];
    public static Scanner data = new Scanner(System.in);
	private static Scanner option;
    public static int columnLength;
    public static int rounds;
    public static int optionMenu;
    
    public static String[][] SBox = {
    {"63","7C","77","7B","F2","6B","6F","C5","30","01","67","2B","FE","D7","AB","76"},
    {"CA","82","C9","7D","FA","59","47","F0","AD","D4","A2","AF","9C","A4","72","C0"},
    {"B7","FD","93","26","36","3F","F7","CC","34","A5","E5","F1","71","D8","31","15"},
    {"04","C7","23","C3","18","96","05","9A","07","12","80","E2","EB","27","B2","75"},
    {"09","83","2C","1A","1B","6E","5A","A0","52","3B","D6","B3","29","E3","2F","84"},
    {"53","D1","00","ED","20","FC","B1","5B","6A","CB","BE","39","4A","4C","58","CF"},
    {"D0","EF","AA","FB","43","4D","33","85","45","F9","02","7F","50","3C","9F","A8"},
    {"51","A3","40","8F","92","9D","38","F5","BC","B6","DA","21","10","FF","F3","D2"},
    {"CD","0C","13","EC","5F","97","44","17","C4","A7","7E","3D","64","5D","19","73"},
    {"60","81","4F","DC","22","2A","90","88","46","EE","B8","14","DE","5E","0B","DB"},
    {"E0","32","3A","0A","49","06","24","5C","C2","D3","AC","62","91","95","E4","79"},
    {"E7","C8","37","6D","8D","D5","4E","A9","6C","56","F4","EA","65","7A","AE","08"},
    {"BA","78","25","12","1C","A6","B4","C6","E8","DD","74","1F","4B","BD","8B","8A"},
    {"70","3E","B5","66","48","03","F6","0E","61","35","57","B9","86","C1","1D","9E"},
    {"E1","F8","98","11","69","D9","8E","94","9B","1E","87","E9","CE","55","28","DF"},
    {"8C","A1","89","0D","BF","E6","42","68","41","99","2D","0F","B0","54","BB","16"}};
    
    public static String[][] InvSBox = {
    {"52","09","6A","D5","30","36","A5","38","BF","40","A3","9E","81","F3","D7","FB"},
    {"7C","E3","39","82","9B","2F","FF","87","34","8E","43","44","C4","DE","E9","CB"},
    {"54","7B","94","32","A6","C2","23","3D","EE","4C","95","0B","42","FA","C3","4E"},
    {"08","2E","A1","66","28","D9","24","B2","76","5B","A2","49","6D","8B","D1","25"},
    {"72","F8","F6","64","86","68","98","16","D4","A4","5C","CC","5D","65","B6","92"},
    {"6C","70","48","50","FD","ED","B9","DA","5E","15","46","57","A7","8D","9D","84"},
    {"90","D8","AB","00","8C","BC","D3","0A","F7","E4","58","05","B8","B3","45","06"},
    {"D0","2C","1E","8F","CA","3F","0F","02","C1","AF","BD","03","01","13","8A","6B"},
    {"3A","91","11","41","4F","67","DC","EA","97","F2","CF","CE","F0","B4","E6","73"},
    {"96","AC","74","22","E7","AD","35","85","E2","F9","37","E8","1C","75","DF","6E"},
    {"47","F1","1A","71","1D","29","C5","89","6F","B7","62","0E","AA","18","BE","1B"},
    {"FC","56","3E","4B","C6","D2","79","20","9A","DB","C0","FE","78","CD","5A","F4"},
    {"1F","DD","A8","33","88","07","C7","31","B1","12","10","59","27","80","EC","EF"},
    {"60","51","7F","A9","19","B5","4A","0D","2D","E5","7A","9F","93","C9","9C","EF"},
    {"A0","E0","3B","4D","AE","2A","F5","B0","C8","EB","BB","3C","83","53","99","61"},
    {"17","2B","04","7E","BA","77","D6","26","E1","69","14","63","55","21","0C","7D"}};
    
    public static String[][] encryptTable = {
    {"01","03","05","0f","11","33","55","ff","1A","2E","72","96","A1","F8","13","35"},
    {"5F","E1","38","48","D8","73","95","A4","F7","02","06","0A","1E","22","66","AA"},
    {"E5","34","5C","E4","37","59","EB","26","6A","BE","D9","70","90","AB","E6","31"},
    {"53","F5","04","0C","14","3C","44","CC","4F","D1","68","B8","D3","6E","B2","CD"},
    {"4C","D4","67","A9","E0","3B","4D","D7","62","A6","F1","08","18","28","78","88"},
    {"83","9E","B9","D0","6B","BD","DC","7F","81","98","B3","CE","49","DB","76","9A"},
    {"B5","C4","57","F9","10","30","50","F0","0B","1D","27","69","BB","D6","61","A3"},
    {"FE","19","2B","7D","87","92","AD","EC","2F","71","93","AE","E9","20","60","A0"},
    {"FB","16","3A","4E","D2","6D","B7","C2","5D","E7","32","56","FA","15","3F","41"},
    {"C3","5E","E2","3D","47","C9","40","C0","5B","ED","2C","74","9C","BF","DA","75"},
    {"9F","BA","D5","64","AC","EF","2A","7E","82","9D","BC","DF","7A","8E","89","80"},
    {"9B","B6","C1","58","E8","23","65","AF","EA","25","6F","B1","C8","43","C5","54"},
    {"FC","1F","21","63","A5","F4","07","09","1B","2D","77","99","B0","CB","46","CA"},
    {"45","CF","4A","DE","79","8B","86","91","A8","E3","3E","42","C6","51","F3","0E"},
    {"12","36","5A","EE","29","7B","8D","8C","8F","8A","85","94","A7","F2","0D","17"},
    {"39","4B","DD","7C","84","97","A2","FD","1C","24","6C","B4","C7","52","F6","01"}};
    
    public static String[][] leftTable = {
    {"00","00","19","01","32","02","1A","C6","4B","C7","1B","68","33","EE","DF","03"},
    {"64","04","E0","0E","34","8D","81","EF","4C","71","08","C8","F8","69","1C","C1"},
    {"7D","C2","1D","B5","F9","B9","27","6A","4D","E4","A6","72","9A","C9","09","78"},
    {"65","2F","8A","05","21","0F","E1","24","12","F0","82","45","35","93","DA","8E"},
    {"96","8F","DB","BD","36","D0","CE","94","13","5C","D2","F1","40","46","83","38"},
    {"66","DD","FD","30","DF","06","8B","62","B3","25","E2","98","22","88","91","10"},
    {"7E","6E","48","C3","A3","B6","1E","42","3A","6B","28","54","FA","85","3D","BA"},
    {"2B","79","0A","15","9B","9F","5E","CA","4E","D4","AC","E5","F3","73","A7","57"},
    {"AF","58","A8","50","F4","EA","D6","74","4F","AE","E9","D5","E7","E6","AD","E8"},
    {"2C","D7","75","7A","EB","16","0B","F5","59","CB","5F","B2","9C","A9","51","A0"},
    {"7F","0C","F6","6F","17","C4","49","EC","D8","43","1F","2D","A4","76","7B","B7"},
    {"CC","BB","3E","5A","FB","60","B1","86","3B","52","A1","6C","AA","55","29","9D"},
    {"97","B2","87","90","61","BE","DC","FC","BC","95","CF","CD","37","3F","5B","D1"},
    {"53","39","84","3C","41","A2","6D","47","14","2A","9E","5D","56","F2","D3","AB"},
    {"44","11","92","D9","23","20","2E","89","B4","7C","B8","26","77","99","E3","A5"},
    {"67","4A","ED","DE","C5","31","FE","18","0D","63","8C","80","C0","F7","70","07"}};
    
    public static void main(String[] args) {
        
    	option = new Scanner(System.in);
        int menuOption;
                
        do {
            menu();
            menuOption = option.nextInt();
            
            switch(menuOption) {
                case 1:{
                    menu1();
                    optionMenu = option.nextInt();
                    String[] chain;
                    insertKey();
                    chain = insertPlainText();
                    int i = 0;
                    while(i<chain.length){
                        for(int j=0;j<4;j++){
                            for(int k=0;k<4;k++){
                                m[k][j]=chain[i];
                                i++;
                            }
                        }
                        
                    cipher(m,k);
                    }    
                    
                    break; 
                }

            }
        }while(menuOption!=3);
    }
    
    private static void insertKey() {
        
    	int keyLength = 0;
        
    	switch(optionMenu) {
            case 1:
                keyLength = 4; 
                rounds = 10;
                break;
            case 2:
                keyLength = 6;
                rounds = 12;
                break;
            case 3:
                keyLength = 8;
                rounds = 14;
                break;
        }
    	
        columnLength = keyLength;
        
        System.out.println("\nInsert the Key: \n");
        String key = data.nextLine();
        
        char[] charArrayKey = key.toCharArray();
        int[] lengthAsciiKey = new int[charArrayKey.length];
        String[] lengthHexadecimal = new String[4*keyLength];
        
        for (int i=0;i<lengthAsciiKey.length;i++) {
            lengthAsciiKey[i]= charArrayKey[i];
            lengthHexadecimal[i] = Integer.toHexString(lengthAsciiKey[i]);
        }
         
        k = new String[4][columnLength]; 
        
        for(int i=0;i<4;i++) {
            for(int j=0;j<columnLength;j++) {
                k[i][j]=lengthHexadecimal[(4*j)+i];
                System.out.print(k[i][j]);
            }
            System.out.println();
        }         
    }
    
    private static String[] insertPlainText() {
       System.out.println("\nInsert the Plaintext : \n");
        String message = data.nextLine();
        char[] charArray = message.toCharArray();
        int[] lengthAscii = new int[charArray.length];
        
        int lenghtMax=0;
        for(int i=1;i<10;i++) {
            if(lengthAscii.length<=16*i){
                lenghtMax=i;
                i=10;
            }
        }
                
        String[] lengthHexadecimal = new String[16*lenghtMax];
        for (int i=0;i<charArray.length;i++) {
            lengthAscii[i]= charArray[i];
            lengthHexadecimal[i] = Integer.toHexString(lengthAscii[i]);
        }
        for (int i=lengthAscii.length;i<lengthHexadecimal.length;i++) {
            lengthHexadecimal[i]= "00";
        }
              
        return lengthHexadecimal;
    }
    
    private static void cipher(String[][] M,String[][] K) {
        
    	int cipherLength = 0;
        
        switch(optionMenu) {
            case 1:
                cipherLength = 40; 
                break;
            case 2:
                cipherLength = 48;
                break;
            case 3:
                cipherLength = 56;
                break;
        }
        
        subKeys = new String[4][4+cipherLength];
        
        for(int i=0;i<4;i++) {
            for(int j=0;j<columnLength;j++) {
                subKeys[i][j] = k[i][j];
            }
        }
        
        for (int i=columnLength;i<cipherLength+4;i++) {
            String[] w4 ={subKeys[0][i-4],subKeys[1][i-4],subKeys[2][i-4],subKeys[3][i-4]}; 
            String[] w1 ={subKeys[0][i-1],subKeys[1][i-1],subKeys[2][i-1],subKeys[3][i-1]};
               
            if((i%columnLength)==0){
                
                String[] nw4 = new String[4];
                String[] nw1 = new String[4];
                String Tw4 = new String();
                String Tw1 = new String();
                int [] num4 = new int[32];
                int [] number = new int[32];
                
                for(int k=0;k<4;k++){
                    nw4[k] = String.format("%8s", Integer.toBinaryString(Integer.parseInt(w4[k], 16))).replace(' ', '0');
                    nw1[k] = String.format("%8s", Integer.toBinaryString(Integer.parseInt(w1[k], 16))).replace(' ', '0');
                }
                
                for(int k=0;k<4;k++){
                    Tw4 = Tw4 + nw4[k];
                    Tw1 = Tw1 + nw1[k];
                }
                
                char[] charArray4 = Tw4.toCharArray();
                char[] charArray1 = Tw1.toCharArray();
                for (int l = 0; l < charArray4.length; l++) {
                    if (charArray4[l] == '0') {
                        num4[l] = 0;
                    } else {
                        num4[l] = 1;
                    }    
                }
                for (int l = 0; l < charArray1.length; l++) {
                    if (charArray1[l] == '0') {
                        number[l] = 0;
                    } else {
                        number[l] = 1;
                    }    
                }
                
                int[] xor41 = xor(num4,funcionT(number,i));
                int length = xor41.length/8;
                String[] xor41T = new String[length];
                
                for(int k=0;k<length;k++) {
                    xor41T[k] = Integer.toString(xor41[(k*8)+0]);
                    xor41T[k] = xor41T[k] + Integer.toString(xor41[(k*8)+1]);
                    xor41T[k] = xor41T[k] + Integer.toString(xor41[(k*8)+2]);
                    xor41T[k] = xor41T[k] + Integer.toString(xor41[(k*8)+3]);
                    xor41T[k] = xor41T[k] + Integer.toString(xor41[(k*8)+4]);
                    xor41T[k] = xor41T[k] + Integer.toString(xor41[(k*8)+5]);
                    xor41T[k] = xor41T[k] + Integer.toString(xor41[(k*8)+6]);
                    xor41T[k] = xor41T[k] + Integer.toString(xor41[(k*8)+7]);
                }

                int[] xor41F = new int[xor41T.length];
                
                for(int k=0;k<xor41T.length;k++) {
                    xor41F[k] = Integer.parseInt(xor41T[k],2);
                }
                String[] xor41A = new String[length];
                
                for(int k=0;k<xor41T.length;k++) {
                    xor41A[k] = Integer.toHexString(xor41F[k]);
                }

                for(int j=0;j<4;j++) {
                 subKeys[j][i] = String.format("%2s", xor41A[j]).replace(' ', '0');   
                }
                
            }
            
            else {
                String[] nw4 = new String[4];
                String[] nw1 = new String[4];
                String Tw4 = new String();
                String Tw1 = new String();
                int [] num4 = new int[32];
                int [] num1 = new int[32];
                
                for(int k=0;k<4;k++) { 
                    nw4[k] = String.format("%8s", Integer.toBinaryString(Integer.parseInt(w4[k], 16))).replace(' ', '0');
                    nw1[k] = String.format("%8s", Integer.toBinaryString(Integer.parseInt(w1[k], 16))).replace(' ', '0');
                }
                
                for(int k=0;k<4;k++) {
                    Tw4 = Tw4 + nw4[k];
                    Tw1 = Tw1 + nw1[k];
                }
                
                char[] charArray4 = Tw4.toCharArray();
                char[] charArray1 = Tw1.toCharArray();
                
                for (int l = 0; l < charArray4.length; l++) {
                    if (charArray4[l] == '0') {
                        num4[l] = 0;
                    } else {
                        num4[l] = 1;
                    }    
                }
                for (int l = 0; l < charArray1.length; l++) {
                    if (charArray1[l] == '0') {
                        num1[l] = 0;
                    } else {
                        num1[l] = 1;
                    }    
                }
                
                int[] xor41 = xor(num4,num1);
                
                int length = xor41.length/8;
                String[] xor41T = new String[length];
                
                for(int k=0;k<length;k++) {
                    xor41T[k] = Integer.toString(xor41[(k*8)+0]);
                    xor41T[k] = xor41T[k] + Integer.toString(xor41[(k*8)+1]);
                    xor41T[k] = xor41T[k] + Integer.toString(xor41[(k*8)+2]);
                    xor41T[k] = xor41T[k] + Integer.toString(xor41[(k*8)+3]);
                    xor41T[k] = xor41T[k] + Integer.toString(xor41[(k*8)+4]);
                    xor41T[k] = xor41T[k] + Integer.toString(xor41[(k*8)+5]);
                    xor41T[k] = xor41T[k] + Integer.toString(xor41[(k*8)+6]);
                    xor41T[k] = xor41T[k] + Integer.toString(xor41[(k*8)+7]);
                }

                int[] xor41F = new int[xor41T.length];

                for(int k=0;k<xor41T.length;k++) {
                    xor41F[k] = Integer.parseInt(xor41T[k],2);
                }
                String[] xor41A = new String[length];
                
                for(int k=0;k<xor41T.length;k++) {
                    xor41A[k] = Integer.toHexString(xor41F[k]);
                }

                for(int j=0;j<4;j++) {
                 subKeys[j][i]=subKeys[j][i] = String.format("%2s", xor41A[j]).replace(' ', '0');   
                }
            }
        }
        
        String[][] cipherText = new String[4][4];
        cipherText = ARK(m, k);
        
        for(int r=1;r<rounds;r++){
            cipherText = SB(cipherText);
            cipherText = SR(cipherText);         
            cipherText = MC(cipherText);
            cipherText = ARK(cipherText, generateRoundKey(r));
        }
        cipherText = SB(cipherText);
        cipherText = SR(cipherText);
        cipherText = ARK(cipherText, generateRoundKey(10));
        
        System.out.println("Cipher Text");
        for(int i=0;i<4;i++) {
            for(int j=0;j<4;j++) {
                System.out.print(cipherText[i][j] + (" "));
            }
        }
            
    }
    
    private static void menu() {
    	
        System.out.println("1. Encrypt Message");
        
    }
    
    private static void menu1() {
    	System.out.println("");
        System.out.println("Select the key bits");
        System.out.println("   1. 128");
        System.out.println("   2. 192");
        System.out.println("   3. 256");

    }
    
    private static String[][] ARK(String[][] m,String[][]k){
        String[][] temporary = new String[4][4];
        
        for(int i=0;i<4;i++){
            for(int j=0;j<4;j++){
                
                String text1 = String.format("%8s", Integer.toBinaryString(Integer.parseInt(m[i][j], 16))).replace(' ', '0');
                String text2 = String.format("%8s", Integer.toBinaryString(Integer.parseInt(k[i][j], 16))).replace(' ', '0');
                                
                char[] textArray1 = text1.toCharArray();
                char[] textArray2 = text2.toCharArray();
                
                int[] binaryText1 = new int[textArray1.length];
                int[] binaryText2 = new int[textArray2.length];
                
                for(int l=0;l<binaryText1.length;l++) {
                    if(textArray1[l]=='0'){
                        binaryText1[l] = 0;
                    }
                    else{
                        binaryText1[l] = 1;
                    }   
                }
                
                for(int l=0;l<binaryText2.length;l++) {
                    if(textArray2[l]=='0'){
                        binaryText2[l] = 0;
                    }
                    else{
                        binaryText2[l] = 1;
                    }        
                }
                
                int[] xOr = xor(binaryText1,binaryText2);
                
                String binary1 = Integer.toString(xOr[0])+Integer.toString(xOr[1])+Integer.toString(xOr[2])+Integer.toString(xOr[3]);
                String binary2 = Integer.toString(xOr[4])+Integer.toString(xOr[5])+Integer.toString(xOr[6])+Integer.toString(xOr[7]);
                                
                String hexadecimal1 = Integer.toHexString(Integer.parseInt(binary1, 2));
                String hexadecimal2 = Integer.toHexString(Integer.parseInt(binary2, 2));
                
                String total= hexadecimal1+hexadecimal2;
                temporary[i][j]=total;
            }
        }
        return temporary;
    }
    
    private static String[][] SB(String[][] M){
        String[][] temporary = new String[4][4];
        
        for(int i=0;i<4;i++) {
            for(int j=0;j<4;j++) {
            	
                char[] array = M[i][j].toCharArray();
                int decimal1=Integer.parseInt(Character.toString(array[0]), 16);
                int decimal2=Integer.parseInt(Character.toString(array[1]), 16);
                
                temporary[i][j] = SBox[decimal1][decimal2]; 
            }
        }
        return temporary;
    }
    
    private static String[][] SR(String[][]M){ 
        
      String[][] temporary = new String[4][4];
      
      for (int j=0;j<4;j++) {
        temporary[0][j] = M[0][j];          
      }
      
      temporary[1][3] = M[1][0];
      
      for (int j=0;j<3;j++){
        temporary[1][j] = M[1][j+1];          
      }
      
      temporary[2][0] = M[2][2];
      temporary[2][1] = M[2][3];
      temporary[2][2] = M[2][0];
      temporary[2][3] = M[2][1];
      temporary[3][0] = M[3][3];
      
      for (int j=1;j<4;j++) {
        temporary[3][j] = M[3][j-1];          
      }    
      return temporary;
    }
    
    private static String[][] MC(String[][] M) {
    	
        String[][] temporary = new String[4][4];
        int[][][] polinomyals = {{{0,2},{0,3},{0,1},{0,1}},{{0,1},{0,2},{0,3},{0,1}},{{0,1},{0,1},{0,2},{0,3}},{{0,3},{0,1},{0,1},{0,2}}};                
        String[] column1 = new String[4];
        int[][] column2 = new int[4][2];
        
        for (int i=0;i<4;i++) {
            int[][] order = new int[4][8];
            for(int j=0;j<4;j++){
                 column1[j] = M[j][i];
                 char[] charArray = column1[j].toCharArray();
                 column2[j][0] = Integer.parseInt(Character.toString(charArray[0]),16);
                 column2[j][1] = Integer.parseInt(Character.toString(charArray[1]),16);       
            } 
            for(int k =0; k<4;k++) {
                
            	String leftColumn = leftTable[column2[k][0]][column2[k][1]];
                String leftPolynomium = leftTable[polinomyals[i][k][0]][polinomyals[i][k][1]];
                String resultedString = String.format("%8s",Integer.toHexString((Integer.parseInt(leftColumn, 16)+Integer.parseInt(leftPolynomium, 16))%255)).replace(' ', '0');
                char[] resultedArray = resultedString.toCharArray();
                int dec1 = Integer.parseInt(Character.toString(resultedArray[0]),16);
                int dec2 = Integer.parseInt(Character.toString(resultedArray[1]),16);
                String result = encryptTable[dec1][dec2];
                String rightBinary = String.format("%8s", Integer.toBinaryString(Integer.parseInt(result, 16))).replace(' ', '0');
                char[] charBinaryR = rightBinary.toCharArray();
                int[] intBinaryR = new int [8];
                
                for(int m=0;m<intBinaryR.length;m++) {
                    for(int n=0;n<intBinaryR.length;n++) { 
                        if(charBinaryR[i]=='0') {
                            intBinaryR[i]=0;
                        }else {
                            intBinaryR[i]=1;
                        }
                    }
                }
                
                order[k]=intBinaryR;
                int[] xorResult=xor((xor(order[0],order[1])),(xor(order[2],order[3])));
                String bin1 = Integer.toString(xorResult[0])+Integer.toString(xorResult[1])+Integer.toString(xorResult[2])+Integer.toString(xorResult[3]);
                String bin2 = Integer.toString(xorResult[4])+Integer.toString(xorResult[5])+Integer.toString(xorResult[6])+Integer.toString(xorResult[7]);
                String hex1=Integer.toHexString(Integer.parseInt(bin1, 2));
                String hex2=Integer.toHexString(Integer.parseInt(bin2, 2)); 
                String total= hex1+hex2;
                temporary[i][k]=total;
            }
            
        }
        
        return temporary;
    }
    
    private static int[] xor(int[] a, int[] b) {
        int[] temporary = new int[a.length];
        for (int i = 0; i < a.length; i++) {
            if (a[i] == b[i]) {
                temporary[i] = 0;
            } else {
                temporary[i] = 1;
            }
        }
        return temporary;
    }
    
    private static int[] funcionT (int[] w1 , int indice){
        switch(optionMenu){
            case 1:
			break;
            case 2:
			break;
            case 3:
			break;
        }
        String[] w1pos = new String[4];
        String[] w1posF = new String[4];
        for(int k=0;k<w1pos.length;k++){
            w1pos[k] = Integer.toString(w1[(k*8)+0]);
            w1pos[k] = w1pos[k] + Integer.toString(w1[(k*8)+1]);
            w1pos[k] = w1pos[k] + Integer.toString(w1[(k*8)+2]);
            w1pos[k] = w1pos[k] + Integer.toString(w1[(k*8)+3]);
            w1pos[k] = w1pos[k] + Integer.toString(w1[(k*8)+4]);
            w1pos[k] = w1pos[k] + Integer.toString(w1[(k*8)+5]);
            w1pos[k] = w1pos[k] + Integer.toString(w1[(k*8)+6]);
            w1pos[k] = w1pos[k] + Integer.toString(w1[(k*8)+7]);
        }
        
        
        String[] w1B = {w1pos[1],w1pos[2],w1pos[3],w1pos[0]};
        
        for (int i=0;i<w1B.length;i++){
            int temp;
            temp = Integer.parseInt(w1B[i],2);
            String numHexa=String.format("%2s", Integer.toHexString(temp)).replace(' ', '0');
            char[] tempC = numHexa.toCharArray();
            int one = Integer.parseInt(Character.toString(tempC[0]),16);
            int two = Integer.parseInt(Character.toString(tempC[1]),16);
            String binary = Integer.toBinaryString(Integer.parseInt(SBox[one][two],16));
            w1posF[i] = binary;
        }
        
        String total = w1posF[0]+ w1posF[1]+w1posF[2]+w1posF[3];
        char[] temporal = total.toCharArray();
        int[] w1F = new int[32];
        
        for (int i=0;i<temporal.length;i++) {
            if (temporal[i]=='0') {
                w1F[i] = 0;
            }
            else {
                w1F[i] = 1;
            }
        }
        
        int powIndex=(indice-columnLength)/columnLength;
        int pow;
        
        if(powIndex==8) {
            pow=27;
        }else{
            if(powIndex==9){
                pow=54;
            }
            else{
                pow= (int) Math.pow(2,powIndex);
            }
        }
        String hexa = String.format("%2s", Integer.toHexString(pow)).replace(' ', '0');
        
        hexa = hexa + "0"+ "0"+ "0"+ "0"+ "0"+ "0";
        char[] hexaor = hexa.toCharArray();
        String [] stringhexaor = new String[hexaor.length];
        for(int i=0;i<stringhexaor.length;i++){
            stringhexaor[i]=Character.toString(hexaor[i]);
            
        }
        String [] stringbinor = new String[stringhexaor.length];
        
        for(int i=0;i<stringbinor.length;i++) {
            stringbinor[i]=String.format("%4s", Integer.toBinaryString(Integer.parseInt(stringhexaor[i], 16))).replace(' ', '0');;  
        }
        String finalBinaryString=stringbinor[0];
        for(int i=1;i<stringbinor.length;i++) { 
            finalBinaryString= finalBinaryString+stringbinor[i];
        }
        
        char[] charArrayFinal = finalBinaryString.toCharArray();
        int[] finalBinary = new int[32];
        
        for(int i=0;i<finalBinary.length;i++) {
            if(charArrayFinal[i]=='0'){
                finalBinary[i] = 0;
            }else{
                finalBinary[i] = 1;
            }
        }
        
        return finalBinary;
    }
    
    public static String[][] generateRoundKey(int index) {
        String[][] temporary = new String[4][4];
        
        for(int i=0;i<4;i++) {
            temporary[i][0]=subKeys[i][4*index];
            temporary[i][1]=subKeys[i][4*index+1];
            temporary[i][2]=subKeys[i][4*index+2];
            temporary[i][3]=subKeys[i][4*index+3];
        }
        return temporary;
    }
    
}