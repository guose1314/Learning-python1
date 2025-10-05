# -*- coding: utf-8 -*-
"""
@author: mattia
"""
import math
import numpy as np
import matplotlib.pyplot as plt

class TrajectoryFollower():
    """
    Trajectory following algorithm implementation. Pure Pursuit
    2 controllers: One PI for speed and one P for orientation
    """

    @staticmethod
    def next_state(X,u,dt,L,gamma_max):
        """
        Very simple bicycle kinematic model for vehicle.
        Arguments:
            X: State (x,y,theta)
            u: Input (v, gamma)
            dt: Time step
            L: Vehicle's length
            gamma_max: Maximum steering angle
        Output:
            X_next: Next state
        """
        x, y, theta = X[0], X[1], X[2]
        v, gamma = u[0], u[1]

        if gamma > gamma_max:
            gamma = gamma_max
        if gamma < -gamma_max:
            gamma = -gamma_max

        x_next = x + v * np.cos(theta) * dt
        y_next = y + v * np.sin(theta) * dt
        theta_next = theta + (v / L) * np.tan(gamma) * dt

        X_next = [x_next, y_next, theta_next]
        return X_next

    @staticmethod
    def distance(X1, X2):
        """
        Arguments:
            X1: (x1, y1, theta1)
            X2: (x2, y2, theta2)
        Output:
            Euclidean distance between the two points
        """
        return np.sqrt((X1[0] - X2[0])**2 + (X1[1] - X2[1])**2)


    @staticmethod
    def find_closest_wp(X, traj):
        """
        Returns index of the closest waypoint on traj from X
        Input:
            X: Vehicle's state. X = [x, y, theta]
            traj: List of Waypoints of type waypoint.
        Output:
            wp_min.i: Index of the closest waypoint
            d_min: Distance of the closest waypoint
        """

        wp_min = traj[0]
        d_min = TrajectoryFollower.distance(X, [traj[0].x, traj[0].y])

        for wp in traj:
            d = TrajectoryFollower.distance(X, [wp.x, wp.y])
            if d < d_min:
                d_min = d
                wp_min = wp

        return wp_min.i, d_min

    @staticmethod
    def find_next_wp(X, traj, look_ahead_dist):
        """
        Returns the target waypoint as defined as in the Pure Pursuit method. Think carrot and donkey.
        Input:
            X = [x, y, theta]: Current state
            traj: List of waypoints of type waypoint
            look_ahead_dist: Look ahead distance
        Output:
            wp_target: Target waypoint
        """

        # Find closest waypoint
        i_closest, d_closest = TrajectoryFollower.find_closest_wp(X, traj)
        wp_closest = traj[i_closest]

        # Case 1: We are close to path and the circle around X intersects the trajectory to follow
        if d_closest < look_ahead_dist:

            d_max = d_closest
            wp_target = wp_closest
            # Loop starting from the wp_closest
            target_wp_found = False
            i = wp_closest.i
            while target_wp_found == False:
                wp = traj[i]
            # for wp in traj[wp_closest.i:]:
                # Compute distance between the wp and our position
                d = TrajectoryFollower.distance(X, [wp.x, wp.y])
                if d > d_max and d < look_ahead_dist:
                    d = d_max
                    wp_target = wp
                elif d > d_max and d > look_ahead_dist:
                    d = d_max
                    wp_target = wp
                    target_wp_found = True

                i += 1


        # Case 2: We are far from the traj and the circle around X does not intersects the trajectory to follow
        # In that case, the target waypoint is the closest waypoint. This can be done differently

        else:
            wp_target = wp_closest


        return wp_target


    def follow_traj(self, X_0, traj, params):
        """
        Arguments:
            X_0: (x_0, y_0, theta_0) Initial position
            traj: Trajectory to follow. List of waypoints of type waypoint
            params: [dt, L, Ki, Kh, Kv, gamma_max, look_ahead_dist]
                dt: Time step
                L: Vehicle's length
                Ki: Integral gain speed controller
                Kv: Proportional gain speed controller
                Kh: Proportional gain steering controller
                gamma_max: Maximum steering angle
                look_ahead_dist: Look ahead distance
        Output:
            traj_x: List of all x
            traj_y: List of all y
            traj_theta: List of all theta

        """
        dt, L, Ki, Kh, Kv, gamma_max, look_ahead_dist = params[0], params[1], params[2], params[3], params[4], params[5], params[6]

        # List of states
        list_X = [X_0]

        # Integral error used for PID
        error_int = 0

        # For loop with no physical meaning. We could replace with with many things
        for i in range(6500):

            # Current state
            X = list_X[-1]
            x, y, theta = X[0], X[1], X[2]

            # Target waypoint
            wp_star = TrajectoryFollower.find_next_wp(X, traj, look_ahead_dist)

            # Distance from this target waypoint
            dist = TrajectoryFollower.distance(X, [wp_star.x, wp_star.y])

            # Error used in the PI controller for speed
            error =  dist - look_ahead_dist

            # PI Controller
            error_int += error * dt
            v = Kv * error + Ki * error_int

            # Yaw target angle = direction of the target waypoint
            theta_s = math.atan2(wp_star.y - X[1], wp_star.x - X[0])

            # Steering wheel angle
            gamma = Kh * (theta_s - theta)
            gamma = (gamma + np.pi) % (2 * np.pi ) - np.pi

            # Control input
            u = [v, gamma]

            # Compute next state
            X_next = TrajectoryFollower.next_state(X,u,dt,L,gamma_max)
            list_X.append(X_next)



        traj_x = [X[0] for X in list_X]
        traj_y = [X[1] for X in list_X]
        traj_theta = [X[2] for X in list_X]


        return traj_x, traj_y, traj_theta
