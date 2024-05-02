#Oluwatodimu Olaleye
#2087951

def get_age():
    age = int(input())
    if age < 18:
        raise ValueError("Invalid age.")
    if age > 75:
        raise ValueError("Invalid age.")
    return age


def fat_burning_heart_rate(age):
    heart_rate = (220 - age) * 0.70
    return heart_rate


if __name__ == "__main__":
    try:
        age = get_age()
        heart_rate = fat_burning_heart_rate(age)
        print(f"Fat burning heart rate for a {age} year-old: {heart_rate} bpm")
    except ValueError as excpt:
        print(f'{excpt}')
        print("Could not calculate heart rate info.")
        print()
