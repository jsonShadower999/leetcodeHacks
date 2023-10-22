public static void removespace(String str1) {
        //String s11=str1.replace(" ","");

        char[] ch1 = str1.toCharArray();
        String res = "";
        for (int i = 0; i < ch1.length; i++) {
            if (!Character.isWhitespace(ch1[i])) {
                res = res + ch1[i];

            }


        }
        System.out.println(res);


    }
