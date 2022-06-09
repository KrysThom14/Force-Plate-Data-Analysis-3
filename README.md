# Force-Plate-Data-Analysis-3
This was initially part of an assignment I had from grad school (Exercise Science) in my Biomechanics class. This is just a result of me taking a deeper dive into the analysis of the data using Python. This part of the assignment had to do with analyzing a ~5sec. recording of someone performing 3 separate Bilateral Countermovement Jumps. Each jump was recorded at a different frequency (100Hz, 500Hz, 1000Hz), on a Force Plate. For simplicity purposes, it is assumed that all 3 jumps are exactly the same. Because this is a vertical jump, we are only concerned with forces in the Z direction (vertical). 

I have the results of the calculations in each section commented out, as well as the calculations themselves so that I can run one at a time. You would only need to change the location where the sheet is located when creating the dataframes if you were to run these calculations on your own computer. 


### Importing Data Frames & Calculating Aggregates
* I imported all 3 data frames, which look very similar to my other force plate analysis projects. I then calculated mean, median, min, etc. for all 3 data frames and compared them.

![CM_Jump-1](https://user-images.githubusercontent.com/94875597/172931797-a175116c-33c9-48f1-97db-df6c5f1b0330.png)


### Visualizing Differences
* I graphed the previous calculations to see any differences. This image just shows the differences in the maxes (a.k.a. landing from the jump).

![CM_Jump-2](https://user-images.githubusercontent.com/94875597/172933053-e4b99961-71f0-4bd7-a9ef-e7f8d71182dd.png)

![CM_Jump-3](https://user-images.githubusercontent.com/94875597/172933068-b3a99419-b2d7-4045-919f-09bf4fb05998.png)


### Why Frequency Matters
* When the Z Forces from the 3 data frames are graphed side by side, you can see the vast difference there is in the amount of data collected from the same 5sec. jump. When studying something that happens so quickly, the faster the data is recorded (500Hz vs. 1,000Hz) the more likely you are to get the true values of what occurred in the test. At least to a degree.

![CM_Jump-4](https://user-images.githubusercontent.com/94875597/172934455-0c470713-a645-410f-91c0-85c72569526f.png)

![CM_Jump-5](https://user-images.githubusercontent.com/94875597/172934472-60348b0b-9ec5-47f0-92b5-0bf35c243dd9.png)

