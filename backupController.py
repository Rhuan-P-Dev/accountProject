import os
import schedule
import time
import threading

from pathController import PathController

Path = PathController()

class BackupController:
    def __init__(self):
        self.backup_frequency = 1

    def backup(self):
        try:
            import shutil
            import datetime
            timestamp = datetime.datetime.now()
            backup_dir = os.path.join(
                Path.pathToAllObjects,
                "backup",
                str(timestamp.year),
                str(timestamp.month),
                str(timestamp.day),
                str(timestamp.hour),
                str(timestamp.minute)
            )
            os.makedirs(backup_dir, exist_ok=True)
            shutil.copytree(Path.pathToMonthObjects, os.path.join(backup_dir, "monthObjects"))
            shutil.copytree(Path.pathToMonthsObjects, os.path.join(backup_dir, "monthsObjects"))
            shutil.copytree(Path.pathToInfObjects, os.path.join(backup_dir, "infObjects"))
        except Exception as e:
            print("Error while creating backup: ", str(e))

    def schedule_backup(self):
        schedule.every(
            self.backup_frequency
        ).hours.do(self.backup)

        while True:
            schedule.run_pending()
            time.sleep(1)

    def start_backup_scheduler(self):
        thread = threading.Thread(
            target=self.schedule_backup
        )
        thread.start()