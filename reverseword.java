 public static void reverseword(String str1) {
        char ch1[] = str1.toCharArray();
        String res = "";
        for (int i = ch1.length - 1; i >= 0; i--) {
            res = res + ch1[i];

        }
        System.out.println(res);

        // use two pointer
    }
