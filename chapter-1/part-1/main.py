def destroy_walls(wall_health):
    for hp in wall_health:
        if hp <= 0:
            wall_health.remove(hp)
    return wall_health
