import javax.crypto.Cipher;
import javax.crypto.SecretKey;
import javax.crypto.SecretKeyFactory;
import javax.crypto.spec.DESKeySpec;
import java.security.SecureRandom;

public class DES {
	// Const to call implemented DES algorithm with SecretKeyFactory class
	private final static String DES = "DES";
	
	public static void main(String[] args) {
		String message = "Esta mensagem tem um teor de alta periculosidade";
		
		// Encryption using a nounce key
		String key = "19021993";

		String stringEncryption = encryption(message, key);
		System.out.println(stringEncryption);

		String stringDecryption = decryption(stringEncryption, key);
		System.out.println(stringDecryption);
	}
	
	public static byte[] encrypt(byte[] source, byte[] key) throws Exception {

		SecureRandom secureRandom = new SecureRandom();
		
		// Function to create the first 8 bytes in key as the key material for the DES key
		DESKeySpec desKey = new DESKeySpec(key);

		SecretKeyFactory keyFactory = SecretKeyFactory.getInstance(DES);
		SecretKey securekey = keyFactory.generateSecret(desKey);

		Cipher cipher = Cipher.getInstance(DES);

		cipher.init(Cipher.ENCRYPT_MODE, securekey, secureRandom);

		return cipher.doFinal(source);
	}
	
	public static byte[] decrypt(byte[] source, byte[] key) throws Exception {
		
		SecureRandom secureRandom = new SecureRandom();
		
		DESKeySpec desKey = new DESKeySpec(key);
		
		SecretKeyFactory keyFactory = SecretKeyFactory.getInstance(DES);
		SecretKey securekey = keyFactory.generateSecret(desKey);
		
		Cipher cipher = Cipher.getInstance(DES);
		
		cipher.init(Cipher.DECRYPT_MODE, securekey, secureRandom);

		return cipher.doFinal(source);
	}
	
	public final static String encryption(String password, String key) {
		try {
			return byteToString(encrypt(password.getBytes(), key.getBytes()));
		} catch (Exception e) {
		
		}
		return null;
	}
	
	public final static String decryption(String data, String key) {
		try {
			return new String(decrypt(stringTobyte(data.getBytes()), key.getBytes()));
		} catch (Exception e) {
			e.printStackTrace();
		}
		return null;
	}

	public static String byteToString(byte[] bytes) {
		String hash = "";
		String string = "";
		for (int n = 0; n < bytes.length; n++) {
			string = (java.lang.Integer.toHexString(bytes[n] & 0XFF));
			if (string.length() == 1)
				hash = hash + "0" + string;
			else
				hash = hash + string;
		}
		return hash.toUpperCase();
	}
	
	public static byte[] stringTobyte(byte[] bytes) {
		if ((bytes.length % 2) != 0)
			throw new IllegalArgumentException("Error of lenght");
		byte[] stringBytes = new byte[bytes.length / 2];
		for (int number = 0; number < bytes.length; number += 2) {
			String item = new String(bytes, number, 2);
			stringBytes[number / 2] = (byte) Integer.parseInt(item, 16);
		}
		return stringBytes;
	}
}