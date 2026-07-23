def compare_snapshots(old, new):
    changes = []

    all_dates = sorted(set(old.keys()) | set(new.keys()))

    for date in all_dates:

        old_movies = old.get(date, {})
        new_movies = new.get(date, {})

        # New date appeared
        if date not in old:
            changes.append(f"🟢 New booking date: {date}")

        # Date disappeared
        elif date not in new:
            changes.append(f"🔴 Booking date removed: {date}")

        all_movies = sorted(set(old_movies.keys()) | set(new_movies.keys()))

        for movie in all_movies:

            old_count = old_movies.get(movie, 0)
            new_count = new_movies.get(movie, 0)

            if old_count == 0:
                changes.append(f"➕ {movie} added on {date}")

            elif new_count == 0:
                changes.append(f"➖ {movie} removed from {date}")

            elif old_count != new_count:
                changes.append(
                    f"🔄 {movie} changed on {date} ({old_count} → {new_count})"
                )

    return changes