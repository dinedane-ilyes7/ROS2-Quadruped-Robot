"""Source checks only; do not claim simulation or hardware validation."""
import csv
from pathlib import Path
import tarfile
import unittest
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
PKG = ROOT / "ros2_ws" / "src" / "mini_dog"
EXPECTED_JOINTS = {
    f"leg_{leg}{suffix}_joint"
    for leg in range(1, 5) for suffix in ("", "_2", "_3")
}


class ProjectSourceChecks(unittest.TestCase):
    def test_robot_model_has_twelve_revolute_joints(self):
        tree = ET.parse(PKG / "urdf" / "LatestFullRobot.urdf.xacro")
        joints = [el for el in tree.iter("joint") if el.get("type") == "revolute"]
        self.assertEqual(len(joints), 12)
        self.assertEqual({j.get("name") for j in joints}, EXPECTED_JOINTS)

    def test_controller_config_lists_all_joints(self):
        config = (PKG / "config" / "ros2_control.yaml").read_text()
        for joint in EXPECTED_JOINTS:
            self.assertIn("- " + joint + "\n", config)

    def test_servo_calibration(self):
        with (ROOT / "hardware" / "servo_calibration.csv").open(newline="") as f:
            rows = list(csv.DictReader(f))
        self.assertEqual(len(rows), 12)
        self.assertEqual({int(r["pca9685_channel"]) for r in rows},
                         {0, 1, 2, 4, 5, 6, 8, 9, 10, 12, 13, 14})
        for row in rows:
            self.assertLessEqual(int(row["tested_min_pwm_us"]), int(row["standing_pwm_us"]))
            self.assertLessEqual(int(row["standing_pwm_us"]), int(row["tested_max_pwm_us"]))
        self.assertEqual(next(r["standing_pwm_us"] for r in rows if r["pca9685_channel"] == "12"), "1400")

    def test_mesh_archive_has_all_parts(self):
        with tarfile.open(PKG / "meshes.tar.xz", "r:xz") as archive:
            names = {entry.name for entry in archive.getmembers()}
        expected = {"meshes/base_link.stl"} | {
            f"meshes/leg_{leg}{suffix}.stl"
            for leg in range(1, 5) for suffix in ("", "_2", "_3")
        }
        self.assertEqual(names, expected)


if __name__ == "__main__":
    unittest.main()
