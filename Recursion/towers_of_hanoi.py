
def hanoi(n, count, source="A", target="B", auxiliary="C"):
    print(f"hanoi({n}, {count}, {source}, {target}, {auxiliary})")
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        count += 1
        return count
    count = hanoi(n-1, count, source, auxiliary, target)
    print(f"Move disq {n} from {source} to {target}")
    count += 1
    count = hanoi(n-1, count, auxiliary, target, source)
    return count

print("Moves required for 4 disks:")
counter = hanoi(7, 0)
print("Moves required for 3 disks:", counter)
