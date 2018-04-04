import sklearn.gaussian_process as gp

f = open("/data/Lei_student/Hussain/ML/dm6/peakerror/summary.csv", "r")

def bayesian_optimization(n_iters, sample_loss, xp, yp):
      """
      Arguments:
      ----------
      n_iters: int.
        Number of iterations to run the algorithm for.
      sample_loss: function.
        Loss function that takes an array of parameters.
      xp: array-like, shape = [n_samples, n_params].
        Array of previously evaluated hyperparameters.
      yp: array-like, shape = [n_samples, 1].
        Array of values of `sample_loss` for the hyperparameters in `xp`.
     """

     # Define the GP
     kernel = gp.kernels.Matern()
     model = gp.GaussianProcessRegressor(kernel=kernel,
                                        alpha=1e-4, 
                                        n_restarts_optimizer=10,
                                        normalize_y=True) 
     for i in range(n_iters): 
         # Update our belief of the loss function 
         model.fit(xp, yp)                        

         # sample_next_hyperparameter is a method that computes the arg
         # max of the acquisition function
         next_sample = sample_next_hyperparameter(model, yp)
         # Evaluate the loss for the new hyperparameters

         next_loss = sample_loss(next_sample)
