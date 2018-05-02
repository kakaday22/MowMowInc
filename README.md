<h1>Hello World!</h1>
<p>We are Mow Mow Inc, a group of Georgia Tech seniors that worked together to create the basis for developing tools to distinguish mowed vs unmowed grass for an autonomous lawnmower.
<br><br>
We created tools to label images of the different types of grass we came across and build convolution neural network to trained said images and test the neural network to see how well it performs in the real world. 
<br><br>
Disclaimer: the group name was inspired <strike>gracefully</strike> by  Mario Kart's Moo Moo Farm stage.
</p>

<h2>Data Collection</h2>
<p>
  This program consists of a tool to capture and label images according to its grass status: 
  <i>Mowed, Unmowed, Unknown, Irrelevant</i>. 
  The program consist of the following classes to work:
  
  <h3>dataCollection.py</h3>
  <p>Main Runner for data labeling tool to run it call <b><i>python dataCollection.py</i></b> and the GUI will load the images located on the Image folder located on the folder inside Data Collection.
  <br><br>
This class contains all the logics behind each button actuation and backend of the labeling tool</p>
  <h3>mainGUI.py</h3>
  <p>Class that generates all the necesary logic behind the GUI in the creation, configuration, and display of all the elements (buttons, progressbar, layout, etc)</p>
</p>

<h2>Neural Network</h2>
<p>
  <h3>NeuralNet.py</h3>
  <h3>mowmowCNN.py</h3>
  <h3>mowmowCNNEval.py</h3>
</p>

<h2>Demo</h2>
<p>
  <p>This Folder contains all the programs to run the demonstration. Requirements are that you need two computers: One running the NeuralNet.py which does all the predictions and the other one running the lawnmowerSim.py which does all the simulation, preferibly this latter one should run on a raspberry pi, however small modifications can be done to run this on a PC
  <br><br>
  Computer 1: <b><i>python NeuralNet.py</i></b>
  Computer 2: <b><i>python lawnmowerSim.py #</i></b>, where # is either 0 (to run on images already saved on the computer) or 1 (to run live by taking pictures on the spot)
  </p>
  <h3>CNNsftp.py</h3>
  <p>Class used to establish a SSH connection between computers</p>
  <h3>NeuralNet.py</h3>
  <p>Class to run NeuralNetork given some weights of a trained dataset and image provided by another computer</p>
  <h3>easterEgg.py</h3>
  <p>This is an easterEgg :)</p>
  <h3>fetchImageEgg.py</h3>
  <p>This script connects to a GoPro Camera and saves the image to a specified directory
  <br><be>This runs on python3 and accepts an argument when call which is used to save a picture</p>
  <h3>frameOverlayer.py</h3>
  <p>Class that uses a given image and projects and overlay of a specified color depending on the classification of the frame of the image</p>
  <h3>lawnmowerSim.py</h3>
  <p>This class is a lawnmower simulation. It uses a Finite State Machine to simulate a pipeline that at each state a task is perfomed. It starts with no actions until a trigger is flagged and begins the run. Begins by taking a pictures and sends it to a neural network, where the neural network will obtain the predictions and distribute it to its proper states (Mowed, Unmowed, Irrelevant, Unknown) in which those state will gather some parameters that will later be executed by the last state.</p>
  <h3>mowmowCNNPredictor.py</h3>
  <p>Dependency class used on the NeuralNet to come with all the predictions</p>

<h2>Misc Codes</h2>
<p>
  <h3>Camera.py</h3>
  <p>A Camera library made to connect to a USB camera</p>
  <h3>resizeImg.py</h3>
  <p>Script that takes an image and resize it to a specified size</p>
  <h3>videoSlicing.py</h3>
  <p>Script that takes a video and slices each frame and saves it to a specified directory</p>
</p>
