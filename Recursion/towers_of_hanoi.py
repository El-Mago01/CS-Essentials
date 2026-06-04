def hanoi(n, source="A", target="B", auxiliary="C"):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    hanoi(n-1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    hanoi(n-1, auxiliary, target, source)

print("Moves required for 8 disks:")
hanoi(8)
