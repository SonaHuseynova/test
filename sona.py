def find_second_largest(nums):
    if len(nums) < 2:
        print("Siyahıda 2-dən az element var.")
        return None

    first = second = float('-inf')
    print(f"Başlanğıc: first = {first}, second = {second}\n")

    for i, num in enumerate(nums):
        print(f"Addım {i + 1}: Yoxlanılan ədəd = {num}")
        
        if num > first:
            second = first
            first = num
            print(f"  -> {num} > first idi. Yeniləndi: first = {first}, second = {second}")
        elif num > second and num != first:
            second = num
            print(f"  -> {num} > second və first-ə bərabər deyil. Yeniləndi: second = {second}")
        else:
            print(f"  -> Dəyişiklik olmadı.")
        print("-" * 30)

    result = second if second != float('-inf') else None
    print(f"\nNəticə - İkinci ən böyük ədəd: {result}")
    return result

# Test edək:
sayilar = [10, 5, 20, 8, 15]
find_second_largest(sayilar)