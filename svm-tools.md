libsvm tutorial

[livsvm tutorial](https://www.csie.ntu.edu.tw/~cjlin/libsvm/)
```ruby
model = svmtrain(training_label_vector, training_instance_matrix, [, 'libsvm_options']);
[predicted_label, accuracy, decision_values/prob_estimates] = svmpredict(testing_label_vector, testing_instance_matrix, model,[, 'libsvm_options]);
```

[Multi-class fitcecoc](https://au.mathworks.com/help/stats/fitcsvm.html#bt9w6j6-3)
params = hyperparameters('fitcecoc',X,Y);
params(1).Range = [1e-4,1e6];
fitcecoc(X,Y,'OptimizeHyperparameters','auto','Standardize',true)
