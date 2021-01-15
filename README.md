# Simple-Rock-Paper-Scissors-game

This is a single player Rock-Paper-Scissors game where the opponent will be a bot/program which will randomly select a choice between "Rock" "Paper" "Scissors".

You can select your choice as "Rock" "Paper" "Scissors" by choosing "1" "2" "3" respectively.

By comparing your choice with the bot/program the winner will be decided.

The program also maintains a the count of wins, losses and ties you had.

You can quit the game by choosing 0.


**Requirment to play**

* Python 3 installed on your device.


**How to start playing**

Copy/Clone the file to your device and run the following command in the command prompt/terminal : 

      python <absolute_path>/rps.py                # python C:\Users\device_name\Desktop\rps.py
                                                   # python /etc/mnt/c/Users/device_name/Desktop/rps.py

OR

      python <relative_path>/rps.py                # python \device_name\Desktop\rps.py
                                                   # python /device-name/Desktop/rps.py

OR

You can go to the location where the file is saved and you can open the command prompt/terminal there and just type:

      python rps.py


**Create an Appliction Extension (.exe) file and play**

**Requirements** 

* Python 3 installed
* py2exe

To install py2exe just type the following in the terminal:

      pip install py2exe

After fulfilling above requirments 

* Copy/Clone #rps.py# and setup.py file

* Run the setup.py file by using the command : 

      python setup.py py2exe              #you can run by any method given above
      
* It will create a folder named dist (you can rename this folder as Rock-Paper-Scissors or RPS).

* Inside the dist folder there will be a file called "rps" which will be an Application Extension (.exe)

* Click of the file to play the game


