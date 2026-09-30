import sys

if __name__ == "__main__":
    print("=== Player Score Analytics ===")

    scores = []

    for i in range(1, len(sys.argv)):
        try:
            arg_score = int(sys.argv[i])
            scores.append(arg_score)
        except ValueError:
            print(f"Invalid parameter: '{sys.argv[i]}'")

    if len(scores) == 0:
        print(
                "No scores provided. Usage:"
                "python3 ft_score_analytics.py <score1> <score2> ..."
                )
    else:
        print(f"Scores processed: {scores}")
        print(f"Total players: {len(scores)}")
        print(f"Total scaores: {sum(scores)}")
        print(f"Average score: {sum(scores) / len(scores)}")
        print(f"High score: {max(scores)}")
        print(f"Low score: {min(scores)}")
        print(f"Score range: {max(scores) - min(scores)}")
