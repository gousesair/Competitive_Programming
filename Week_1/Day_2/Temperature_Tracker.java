import org.junit.Test;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;
import java.util.ArrayList;

import static org.junit.Assert.*;

public class Temperature_tracker {

    static class TempTracker {

        // fill in the TempTracker class methods below
        
        int a[]=new int[111];
        int maximum=-1,minimum=111,
        ct=0,modefreq=0;
        double mean=0.0;
        ArrayList<Integer> p;
        
        // records a new temperature
        public void insert(int temperature) {
            if(temperature<minimum) minimum=temperature;
            if(temperature>maximum) maximum=temperature;
            mean = ((mean*ct)+temperature)/(ct+1);
            ct++;
            a[temperature]+=1;
            if (modefreq<a[temperature])
            {
                modefreq=a[temperature];
                p=new ArrayList();
                p.add(temperature);
            }
            else if(modefreq==a[temperature])
            {
                p.add(temperature);
            }  
        }

        // returns the highest temp we've seen so far
        public int getMax() {
            return maximum;
        }

        // returns the lowest temp we've seen so far
        public int getMin() {
            return minimum;
        }

        // returns the mean of all temps we've seen so far
        public double getMean() {
            return mean;
        }

        // return a mode of all temps we've seen so far
        public int getMode() {
            return p.get(0);
        }
    }
}