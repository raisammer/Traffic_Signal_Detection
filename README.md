# Traffic_Signal_Detection
//** Prashant rai_project is tthe code file and remaining are the test images **//

TrafficLight_Detector  which can be install in the vehicle

which will show whether you have to "Move" (Green signal sign),

"Stop"(Red signal sign) 

And if sometimess(by mistake) two bulb light glow at a same time then our code will return the value "ERROR"  
As the error will come it will start to produce a sound to the driver
now here you have to take care of the car that mean you have to understand and run at that situation 

Here what i have done that ihave first detected the blue rectangle  as we have assumed that all the traffic lights will have the vlue outground
so firstly we have detected the blue rectangle and then find the coordinates of the rectangle
Then we have use hough circle to detect the number of circle 
& also we have taken those circle which are in the range of rectangle
by inranging the centre coordinate of the circle in the range of the rectangle
this thing we have done so that any outer error like 
similar circle with red, yellow or green will not make any error in the detection of traffic lights
Now we have detected the color of the centre coordinate of the circle 
and according to that print "RED","YELLOW,"Green"
and if more than 1 Leds lights come true 
than it will send the error which will further use as a sound source for the vehicle man

//**THIS IS THE PROJECT OVERVIEW HOW I MADE THE PROJECT**//
For the explaination of the code please refer to the code there i have explaine d in the comments :
//**AND THE REMAINING CODE IS EXPLAINED IN THE CODE ONLY SO PLEASE REFER TO IT***///
