cc_binary(
	name = "sample",
	srcs = ["sample.cpp"],
	deps = [],
)

# cc_library(
# 	name = "sample_lib",
# 	srcs = ["sample_lib.cpp"],
# 	visibility = ["//visibility:public"],
# )
cc_test(
    name = "sample_test",
    srcs = ["sample_test.cpp"],
    deps = ["@googletest//:gtest_main",
			"//:sample",],
)
