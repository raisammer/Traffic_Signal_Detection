# Traffic_Signal_Detection


As with increasing technology and increasing population traffic accidents becoming more common . Sometimes driver ignore the signal and sometime  unconsiousness by driver result into an accident  so to prevent from these accident i have came up with the solution .This should be installed with the vehicle with the requirement of the front camera 


# Consideration
 I have proceeded for my project with one consideration that for every traffic light there should be a blue background  and inside that three signal Red , Green and  Yellow should come .
 
 
# Install Libraries 
For implementing this project you should install following libraries

  * install open cv
  
  * install numpy 
  
  * install pyautogui
  
## WORKING

HERE what i have done in the code :
 
 1.  Firstly i have detected the blue rectangle as we have assumed or we have taken the consideration that the background of the traffic light signal will be "BLUE" and find out the coordinate of the rectangle .

 2.  Then i have use the hough function to detect the number of circles present in the frame .

 3.  Then we have taken those circle which are coming inside that rectangle by inraniging thecentre coordinate of the circle  in the range of the rectangle  (as hough circle function will give us the (x,y) which represent to the centre of the circle ).

 4.  The above mentioned thing we have done to remove the error which can be caused by the circle which are not present inside the system and may have the same color as RED ,GREEN and Yellow

 5.  Now as we know the centre coordinate of the circle which are lying inside the rectangle  so we will now find out the color regarding  to that circle and 

  * If the traffic signal is RED --> our model will detect it by making RED="True" and give a signal to "STOP" the vehicle 

  * If the traffic signal is GReen --> our model will dtect it by making GREEN ="True" and give a signal that you can "Move" your vehicle 

  * If there is problem in the traffic signal where it is detecting multiple signal at the same time (i.e, "red green at the same time")--> Then our system will detect it as Error and will give a alarm to the diver that you have to make the decision of your own at that time 
   
   so, this is all overview of the code how it's working 
   
   
### Which files are representing what??  

Prashant rai_project is the code file and remaining are the test images 

By changing the image path you can check for each image and you can check other iamges of your files too**
   
   
   THANK YOU FOR READING 

###### THE REMAINING CODE IS EXPLAINED IN THE CODE ONLY SO PLEASE REFER TO IT
