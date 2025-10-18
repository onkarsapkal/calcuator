from django.shortcuts import render

def home(request):
    result = None
    num1 = num2 = operator = ""

    if request.method == "POST":
        num1 = request.POST.get("num1")
        operator = request.POST.get("operator")
        num2 = request.POST.get("num2")

        try:
            num1 = float(num1)
            num2 = float(num2)

            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                result = num1 / num2
            elif operator == '%':
                result = num1 % num2
            elif operator == '**':
                result = num1 ** num2
            else:
                result = "Invalid operator"
        except Exception as e:
            result = f"Error: {e}"

    # ✅ Must match the folder path exactly
    return render(request, 'advanced_calculator/home.html', {'result': result})