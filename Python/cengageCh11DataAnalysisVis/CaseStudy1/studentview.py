"""
File: studentview.py
The view for editing and analyzing student scores.
"""
import matplotlib.pyplot as plt
from breezypythongui import EasyFrame

class StudentView(EasyFrame):

    def __init__(self, model):
        """Creates and lays out window components
        to view and manipulate the model's data."""
        EasyFrame.__init__(self)
        self.setSize(500, 200)
        self.model = model

        self.addLabel("Mean", row = 0, column = 0)            
        self.addLabel("Median", row = 1, column = 0)            
        self.addLabel("Mode", row = 2, column = 0)            
        self.addLabel("Standard deviation", row = 3, column = 0)
        

        self.meanFld = self.addFloatField(value = 0.0, row = 0, column = 1, precision = 2)            
        self.medianFld = self.addFloatField(value = 0.0, row = 1, column = 1, precision = 2)            
        self.modeFld = self.addFloatField(value = 0.0, row = 2, column = 1, precision = 1)            
        self.stdFld = self.addFloatField(value = 0.0, row = 3, column = 1, precision = 4)    

        self.addLabel("Data", row = 0, column = 2, sticky = "NEW")
        self.scoreArea = self.addTextArea(text = "", row = 1, column = 2, width = 12, rowspan = 3)
        

        # Create a panel for the buttons to center them in 5 columns
        bp = self.addPanel(row = 5, column = 0, columnspan = 3, background = "black")
        bp.addButton(text = "Edit score", row = 0, column = 0, command = self.editScore)
        bp.addButton(text = "Add score", row = 0, column = 1, command = self.addScore)
        bp.addButton(text = "Delete score", row = 0, column = 2, command = self.deleteScore)
        bp.addButton(text = "Randomize scores", row = 0, column = 3, command = self.randomizeScores)
        bp.addButton(text = "Plot scores", row = 0, column = 4, command=self.plotScores)            # added button to plot scores in the gui
        
        
        # Place the model's contents in the view
        self.refreshData()

    def refreshData(self):
        """Updates the view with the contents of the model."""
        self.setTitle(self.model.getName() + "'s Scores")
        self.meanFld.setNumber(self.model.getMean())
        self.medianFld.setNumber(self.model.getMedian())
        self.modeFld.setNumber(self.model.getMode())
        self.stdFld.setNumber(self.model.getStd())
        self.scoreArea.setText(str(self.model))

    # Event-handling methods

# **********************************************************************************************************************
    # creates a line plot that will open in a separate window
    def plotScores(self):
        """A docstring for the plotScores method"""
        scores = self.model.scores
        
        x_positions = list(range(1, len(scores) + 1))
        y_scores = scores

        plt.figure(figsize=(6,4))
        plt.plot(x_positions, y_scores, marker='*', color='blue', label="Test Scores")
        plt.xlabel("Test Number")
        plt.ylabel("Score")
        plt.grid(True)
        plt.show()

# **********************************************************************************************************************
    def editScore(self):
        """Obtains a new score and its position from the user
        and updates the model and the view."""
        position = self.prompterBox(title="Edit score", promptString="Enter the position (1-based) of the score to edit:")
        position = int(position)    # convert to integer

        if position < 1 or position > len(self.model.scores):
            self.messageBox(title="Invalid position", message="Please enter a valid position.")
            return
        
        # prompt for new score
        new_score = self.prompterBox(title="New Score", promptString=f"Enter the new score for position {position}:")
        new_score = int(new_score)

        # check for valid score range from 0 to 100
        if new_score < 0 or new_score > 100:
            self.messageBox(title="Invalid score", message="Please enter a score between 0 and 100.")
            return
        
        # update the score in the model
        self.model.setScore(position, new_score)

        # refresh the view to show the updated data
        self.refreshData()

# *******************************************************************************************************************************
    def addScore(self):
        """Obtains a new score from the user,
        adds it to the model, and updates the view."""
        # prompt for new score
        new_score = self.prompterBox(title="New score",
                                     promptString="Enter the new score:")
        
        try:
            new_score = int(new_score)
        except ValueError:
            self.messageBox(title="Invalid input", message="Please enter a valid number for the score.")
            return
        
        if new_score < 0 or new_score > 100:
            self.messageBox(title="Invalid score", message="Please enter a score between 0 and 100.")
            return
        
        self.model.addScore(new_score)

        self.refreshData()

# ******************************************************************************************************************************   
    def deleteScore(self):
        """Obtains the position of a score from the user,
        deletes the score at that position from the model,
        and updates the view."""
        position = self.prompterBox(title = "Delete score",
                                    promptString = "Position of the score:")
        self.model.deleteScore(int(position))
        self.refreshData()

# *********************************************************************************************************************************   
    def randomizeScores(self):
        """Obtains the number of scores, lowest score,
        and highest score from the user, randomizes the model's scores,
        and updates the view."""
        self.model.randomizeScores(10, 75, 100)
        self.refreshData()
   
