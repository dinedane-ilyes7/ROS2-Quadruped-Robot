# Kinematic calculation checkpoint

From the later project discussion, for Leg 1, the zero-angle foot position (in the reference model) was numerically recorded as approximately:

```text
p_foot(q=0) = [ 0.04445164, -0.08949154, -0.18653909 ] m
```

For a +5 mm displacement in Z from that starting point, the inverse-kinematics test returned:

```text
q_ik = [ 0.00865530, -0.04059563, 0.07396253 ] rad
FK(q_ik) - p_target: ~1.22e-11 m (norm)
```

These numbers were verified in the earlier local session, **but the exact validated FK/IK implementation is not inside the supplied historical archive**. They are a checkpoint for comparison, not a claim that this repository reproduces the result. The last calculation and robot geometry conventions should be checked against the most recent modified URDF before implementing gait control.
