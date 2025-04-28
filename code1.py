import cv2
import matplotlib.pyplot as plt

image = cv2.imread('image.jpg')

if image is None:
    print("خطأ: لم يتم العثور على الصورة، تأكد من المسار الصحيح.")
else:
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # تحويل الألوان من BGR إلى RGB
    plt.imshow(image)
    plt.axis('off')  # إخفاء المحاور
    plt.show()
