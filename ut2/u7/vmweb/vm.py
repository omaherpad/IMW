from mysql import DB


class VirtualMachine:

    def __init__(self, id):
        self.db = DB("emmet", "78636756dD.", "vmweb")
        sql = f"select * from vmachine where id={id}"
        query = self.db.query(sql)

        self.name = query[0]["name"]
        self.ram = query[0]["ram"]
        self.cpu = query[0]["cpu"]
        self.hdd = query[0]["hdd"]
        self.os = query[0]["os"]
        self.id = id

    def stop(self):
        sql = f"delete from process where vmachine_id={self.id}"
        self.db.run(sql)
        sql = f"update vmachine set status=0 where id={self.id}"
        self.db.run(sql)

    def start(self):
        sql = f"update vmachine set status=1 where id={self.id}"
        self.db.run(sql)

    def suspend(self):
        sql = f"update vmachine set status=2 where id={self.id}"
        self.db.run(sql)
        self.status = 2

    def reboot(self):
        self.stop()
        self.start()

    def get_processes(self):
        sql = "select * from process where vmachine_id=1"
        return self.db.query(sql)

    def run(self, pid, ram, cpu, hdd):
        sql = f"insert into process (pid, ram, cpu, hdd, vmachine_id) values ({pid}, {ram}, {cpu}, {hdd}, {self.id})"
        self.db.run(sql)

    def ram_usage(self):
        ram = 0
        for p in self.get_processes():
            ram += p["ram"]
        return ram * 100 / self.ram

    def cpu_usage(self):
        cpu = 0
        for p in self.get_processes():
            cpu += p["cpu"]
        return cpu * 100 / self.cpu

    def hdd_usage(self):
        hdd = 0
        for p in self.get_processes():
            hdd += p["hdd"]
        return hdd * 100 / self.hdd

    def get_status(self):
        sql = "select status from vmachine where id=1"
        query = self.db.query(sql)
        status = query[0]["status"]
        if status == 0:
            return "Stopped"
        elif status == 1:
            return "Running"
        elif status == 2:
            return "Suspended"

    def __str__(self):
        return """
{} <{}> [{}]
{:.2f}% RAM used | {:.2f}% CPU used | {:.2f}% HDD used
        """.format(
            self.os,
            self.name,
            self.get_status(),
            self.ram_usage(),
            self.cpu_usage(),
            self.hdd_usage()
        )
