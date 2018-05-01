<h1>Hello World!</h1>
<p>We are Mow Mow Inc, a group of Georgia Tech seniors that worked together to create the basis for developing tools to distinguish mowed vs unmowed grass for an autonomous lawnmower.

We created tools to label images of the different types of grass we came across and build convolution neural network to trained said images and test the neural network to see how well it performs in the real world. 

Disclaimer: the group name was inspired <strike>gracefully</strike> by  Mario Kart's Moo Moo Farm stage.</p>

<h2>Data Collection</h2>
<p>
  This program consists of a tool to capture and label images according to its grass status: 
  <i>Mowed, Unmowed, Unknown, Irrelevant</i>. 
  The program consist of the following classes to work:
  
  <h3>dataCollection.py</h3>
  <p>
  datacollection is the main function used to run this program to run it just call <b><i>python dataCollection.py</i></b> on your terminal and the GUI should begin. This file contains all the logic used for this GUI to actuate.
<ul>
  <li>setButtons()</li>
  <ul><li>This function createst lamda functions and assigns it to each button</li></ul>
  <li>toCSV()</li>
  <ul><li>This function saves the current press to a CSV</li></ul>
  <li>nextImg()</li>
  <ul><li>This function calls the next image and updates the GUI</li></ul>
  <li>updateCounter()</li>
  <ul><li>This function updates the counter and saves it to the <i>initialVal.txt</i></li></ul>
</ul>

<h3>mainGUI.py</h3>
</p>
