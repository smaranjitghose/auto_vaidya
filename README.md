<h1 align = "center">Auto Vaidya</h1>

An open source solution for creating end-end web app for employing the power of deep learning in various clinical scenarios like implant detection, pneumonia detection, brain mri segmentation etc.

## Suggestions for PR:

- Please give your PR for the test branch unless requested otherwise by the project maintainer
- Name your PR appropiately
- Ensure that you had already raised an issue for this PR and the project maintainer had approved and assigned you
- In the PR description, typically the following are expected:
    - Dataset Used:
    - Dataset Size:
    - Dataset Source:
    - Link to Colab Notebook: Please ensure you give access for view to anyone with link
    - Your Exploratory Data Analysis [Snapshots of the relevant ones and your inference from that]
    - Any Pre-Processing methods used. [Elaborate on them]
    - Your framework to train
    - Different methods used for training
    - Test/Train Split
    - Results: Please do not simply state test accuracy. Other perfomance metrics like F1 score,etc are expected
    - ** Draw a table to show the comparitive analysis of the performance of the different methods you used
    - Conclusion: Which method you think is best and why?
- A copy of the notebook used for your training is expected inside the ``notebooks/`` directory.
- Please name the notebook as ```name_of_the_problem_your_github_username```
- The model files are expected to be inside a ```models\name_of_your_problem\``` directory
- If you are using TensorFlow 2.0, please give both the h5 as well as saved_model file
- Once your PR, gets approved uptil this, proceed with a follow up pr to integrate it inside the streamlit app. Refer [this](https://github.com/smaranjitghose/img_ai_app_boilerplate) if you are unaware of how to use streamlit and host it
- For the streamlit app, it would be a good practice if you define the function for classification/prediction/regression inside a separate python file say ```your_problem_name.py``` and import it inside ```app.py``` ( Believe me this would save a lot of time otherwise wasted in debugging)
- For the second PR, you are expected to do the above changes and provide screenshots/a small clip of the working model of the app after integrating your model from the previous PR

Entire App on Heroku: https://auto-vaidya.herokuapp.com/
Frontend on  Netlify: autovaidya.netlify.app

