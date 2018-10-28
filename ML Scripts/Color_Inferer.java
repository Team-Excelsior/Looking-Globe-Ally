import com.sun.istack.internal.Nullable;

import javax.imageio.ImageIO;
import java.awt.*;
import java.awt.image.BufferedImage;
import java.awt.image.Raster;
import java.awt.image.SampleModel;
import java.io.File;
import java.io.IOException;

public class Color_Inferer {

    public Color_Inferer(String[] args){
        String file = args[0];
        String color = args[1];
        String prob = "";
        try{
            prob = args[2];
        }catch(NullPointerException e){
            prob=null;
        }

        float[][] arr = new float[360][360];
        try {
            BufferedImage img = ImageIO.read(new File(file));
            switch(color){
                case "RED":
                    for(int i=0;i<360;i++) {
                        for (int j = 0; j < 360; j++) {
                            Color col = new Color(img.getRGB(i, j));
                            float avg_col = col.getRed() - (((float) col.getBlue() + ((float) col.getGreen())) / 2);
                            if(avg_col<0)
                                avg_col = 0.0f;
                            if(prob!=null)
                                avg_col /= 127;
                            System.out.print(avg_col+" ");
                        }
                    }
                    break;

                case "BLUE":
                    for(int i=0;i<360;i++) {
                        for (int j = 0; j < 360; j++) {
                            Color col = new Color(img.getRGB(i, j));
                            float avg_col = col.getBlue() - (((float) col.getRed() + ((float) col.getGreen())) / 2);
                            if(avg_col<0)
                                avg_col = 0.0f;
                            if(prob!=null)
                                avg_col /= 127;
                            System.out.print(avg_col+" ");
                        }
                    }
                    break;

                case "GREEN":
                    for(int i=0;i<360;i++) {
                        for (int j = 0; j < 360; j++) {
                            Color col = new Color(img.getRGB(i, j));
                            float avg_col = col.getGreen() - (((float) col.getBlue() + ((float) col.getRed())) / 2);
                            if(avg_col<0)
                                avg_col = 0.0f;
                            if(prob!=null)
                                avg_col /= 127;
                            System.out.print(avg_col+" ");
                        }
                    }
                    break;
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args){
        new Color_Inferer(args);
    }
}
