import java.security.Security;
import javax.crypto.Cipher;
import javax.crypto.spec.IvParameterSpec;
import javax.crypto.spec.SecretKeySpec;

public class CTRDES {
  public static void main(String[] args) throws Exception {
	  
    Security.addProvider(new org.bouncycastle.jce.provider.BouncyCastleProvider());
    
    byte[] plaintext = "0123456789abcdeffedcba9876543210".getBytes();
    byte[] keyBytes = "12345678".getBytes();
    byte[] ivBytes = "input123".getBytes();
    
    SecretKeySpec key = new SecretKeySpec(keyBytes, "DES");
    IvParameterSpec ivSpec = new IvParameterSpec(ivBytes);
    Cipher cipher = Cipher.getInstance("DES/CTR/NoPadding", "BC");
    cipher.init(Cipher.ENCRYPT_MODE, key, ivSpec);
    
    byte[] cipherText = new byte[cipher.getOutputSize(plaintext.length)];
    int ciphertextLength = cipher.update(plaintext, 0, plaintext.length, cipherText, 0);
    
    ciphertextLength += cipher.doFinal(cipherText, ciphertextLength);
    System.out.println("cipher: " + new String(cipherText));
    
    cipher.init(Cipher.DECRYPT_MODE, key, ivSpec);
    byte[] plainText = new byte[cipher.getOutputSize(ciphertextLength)];
    int plaintextLength = cipher.update(cipherText, 0, ciphertextLength, plainText, 0);
    plaintextLength += cipher.doFinal(plainText, plaintextLength);
    System.out.println("Plaintext : " + new String(plainText));
  
  }
}
