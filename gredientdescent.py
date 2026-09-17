# def update_weight(w_t, learning_rate, gradient):

#     w_next = w_t -(learning_rate * gradient)

#     return w_next

# current_w = 0.5
# eta = 0.01
# grad = 2.0

# new_w = update_weight(current_w, eta, grad)
# print(f"업데이트된 가중치: {new_w}")

def gradient(w):
    return 2 * (w-3)

def gradient_descent(w_init, learning_rate, tolerance, max_iter):
    w = w_init
    history = [w]

    for t in range(max_iter):
        grad = gradient(w)
        w_next = w - (learning_rate * grad)
        history.append(w_next)

        if abs(w_next - w) < tolerance:
            return w_next, t+1, history

        w = w_next

    return w, max_iter, history

if __name__ == "__main__":
    w_opt, steps, history = gradient_descent(
        w_init=0.0,
        learning_rate=0.1,
        tolerance=1e-5,
        max_iter=100
    )
    print(f"최적화 완료 w: {w_opt:.4f} (수렴 스텝: {steps}회)")
        

