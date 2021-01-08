import tushare as ts
import customInput as ci


ts_token = ci.ts_token
ts.set_token(ts_token)
pro = ts.pro_api(ts_token)