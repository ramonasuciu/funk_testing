bench:
	- fl-run-bench test_mweb.py PerformanceTests.test_get_home_page --distribute --simple-fetch
	- export LC_ALL=en_US.UTF-8
	- export LANG=en_US.UTF-8
#	- fl-build-report --html -o . log-distributed/ec2-107-22-194-126.compute-1.amazonaws.com-mweb-bench.xml log-distributed/ec2-184-72-169-37.compute-1.amazonaws.com-mweb-bench.xml


test:
	- fl-run-test -dv --simple-fetch test_mweb.py

clean:
	- find . "(" -name "mweb*" -or -name "log-distributed" -or -name "*.pyc" -or -name "funkload*" ")" -print0 | xargs -0 rm -rf