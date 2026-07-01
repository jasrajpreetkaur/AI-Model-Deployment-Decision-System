#Model Deployment
accuracy=int(input("Accuracy: "))
Precision=int(input("Precision: "))
Recall=int(input("Recall: "))
F1_score=int(input("F1score: "))
Inference_time=int(input("Inference time(ms): "))
Memory_usage=int(input("Memory usage(MB): "))
print(f"Accuracy:{accuracy}\nPrecision:{Precision}\nRecall:{Recall}\nF1_score:{F1_score}\nInference_time:{Inference_time}\nMemory_usage:{Memory_usage}")
print("------------------------------------MODEL DEPLOYMENT----------------------------------------------")
if(accuracy>=90 and Precision>=90 and Recall>=90 and F1_score>=90 and Inference_time<=100 and Memory_usage<=512):
    print("\nRESULT:Production Ready")
else:
    print("\nRESULT: NOT Production Ready")
