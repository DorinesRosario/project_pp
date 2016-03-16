from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt
import random
dict={0:'r',1:'y',2:'g',3:'b'}
i=0
while i<=3:
    actual = []
    predictions = []
    sortroc=open('*.txt','r').readlines()
    for line in sortroc:
        actual.append(float(line.split()[0]))
        predictions.append(float(line.split()[1]))
    false_positive_rate, true_positive_rate, thresholds = roc_curve(actual, predictions)
    roc_auc = auc(false_positive_rate, true_positive_rate)
    plt.plot(false_positive_rate, true_positive_rate, dict[i], label='AUC'+str(i)+' = %0.2f'% roc_auc)
    plt.plot([0,1],[0,1],'r--')
    plt.xlim([-0.1,1.2])
    plt.ylim([-0.1,1.2])
    i=i+1
plt.legend(loc='lower right')
plt.title('Receiver Operating Characteristic')

plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.show()