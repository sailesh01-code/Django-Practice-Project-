# import seaborn as sns
# import matplotlib.pyplot as plt
# import pandas as pd

# # Data for tumor classification performance
# data = {
#     'UNet+ResNet': [96.0, 95.5, 97.1],
#     'UNet+EfficientNet': [97.2, 96.8, 98.3],
#     'UNet+DenseNet': [97.8, 97.1, 98.5],
#     'UNet+InceptionV3': [96.7, 96.0, 97.8]
# }

# # Creating a DataFrame
# df = pd.DataFrame(data, index=['Glioma', 'Meningioma', 'Pituitary Tumor'])

# # Plot heatmap
# plt.figure(figsize=(8, 6))
# sns.heatmap(df, annot=True, cmap='Blues', fmt='.1f', cbar=True)

# # Add labels and title
# plt.title('Tumor Classification Accuracy for Different Models')
# plt.xlabel('Model')
# plt.ylabel('Tumor Type')

# # Show plot
# plt.show()













#Nested If
# age=int(input('Enter your age : '))
# if age>=18:
#     wgt=float(input('Enter your wgt : '))
#     if wgt>=50:
#         print('You are eligible to donate blood')
#     else:
#         print('You are not eligible because of wgt')
# else:
#     print('You are not eligible because of age')



age=int(input("enter your age:"))
if age>=25:
   state= input("enter your state")
   if state=='odisha':
      mark=int(input("enter your avg mark "))
      if mark>=80:
        degree=input('BTech completed or not ? [yes/no]')
        if degree=='yes':
            print('cong! you are eligible for the job')
        else:
         print('you are not eligible beacuse of degree')
      else:
      print('you are not eligible beacuse of degree')
      




















