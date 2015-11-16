{
"directed":false,
"multigraph":true,
"graph":[],
"nodes":[
{"id":"S1","type":"switch","layer":"access","x":291,"y":299.5,"demand":"","cost":"","capacity":""},

{"id":"S2","type":"switch","layer":"access","x":377,"y":300,"demand":"","cost":"","capacity":""},

{"id":"S3","type":"switch","layer":"access","x":490,"y":299,"demand":"","cost":"","capacity":""},

{"id":"S4","type":"switch","layer":"access","x":572.7804565429688,"y":301.387451171875,"demand":"","cost":"","capacity":""},

{"id":"S5","type":"switch","layer":"aggregation","x":330,"y":242.5,"demand":"","cost":"","capacity":""},

{"id":"S6","type":"switch","layer":"aggregation","x":529.5967407226562,"y":239.7475128173828,"demand":"","cost":"","capacity":""},

{"id":"S7","type":"switch","layer":"core","x":426.5,"y":181.5,"demand":"","cost":"","capacity":""},

{"id":"H1","type":"host","x":264.5,"y":338,"demand":"","cost":"","capacity":"","ip": "10.0.0.1", "mac": "00:00:00:00:00:1"},
{"id":"H2","type":"host","x":312,"y":337,"demand":"","cost":"","capacity":"","ip": "10.0.0.2", "mac": "00:00:00:00:00:2"},
{"id":"H3","type":"host","x":351,"y":337.5,"demand":"","cost":"","capacity":"","ip": "10.0.0.3", "mac": "00:00:00:00:00:3"},
{"id":"H4","type":"host","x":395.5,"y":337,"demand":"","cost":"","capacity":"","ip": "10.0.0.4", "mac": "00:00:00:00:00:4"
},{"id":"H6","type":"host","x":515.0240478515625,"y":337.2362365722656,"demand":"","cost":"","capacity":"","ip": "10.0.0.6", "mac": 

"00:00:00:00:00:6"
},{"id":"H5","type":"host","x":470.810546875,"y":337.2362365722656,"demand":"","cost":"","capacity":"","ip": "10.0.0.5", "mac": 

"00:00:00:00:00:5"
},{"id":"H7","type":"host","x":556.051025390625,"y":337.2362365722656,"demand":"","cost":"","capacity":"","ip": "10.0.0.7", "mac": 

"00:00:00:00:00:7"
},{"id":"H8","type":"host","x":594.6881103515625,"y":337.6345520019531,"demand":"","cost":"","capacity":"","ip": "10.0.0.8", "mac": 

"00:00:00:00:00:8"}],
"links":[
{"source":3,"target":13,"capacity":100,"weight":27,"ports":{"S4":3,"H7":1}},
{"source":6,"target":4,"capacity":1000,"weight":27,"ports":{"S7":1,"S5":1}},
{"source":6,"target":5,"capacity":1000,"weight":27,"ports":{"S7":2,"S6":1}},
{"source":4,"target":0,"capacity":100,"weight":27,"ports":{"S5":2,"S1":1}},
{"source":4,"target":1,"capacity":100,"weight":27,"ports":{"S5":3,"S2":1}},
{"source":2,"target":5,"capacity":100,"weight":27,"ports":{"S3":1,"S6":2}},
{"source":5,"target":3,"capacity":100,"weight":27,"ports":{"S6":3,"S4":1}},
{"source":0,"target":7,"capacity":100,"weight":27,"ports":{"S1":2,"H1":1}},
{"source":0,"target":8,"capacity":100,"weight":27,"ports":{"S1":3,"H2":1}},
{"source":1,"target":9,"capacity":100,"weight":27,"ports":{"S2":2,"H3":1}},
{"source":1,"target":10,"capacity":100,"weight":27,"ports":{"S2":3,"H4":1}},
{"source":2,"target":12,"capacity":100,"weight":27,"ports":{"S3":3,"H6":1}},
{"source":2,"target":11,"capacity":100,"weight":27,"ports":{"S3":2,"H5":1}},
{"source":3,"target":14,"capacity":100,"weight":27,"ports":{"S4":2,"H8":1}},
{"source":4,"target":5,"capacity":10,"weight":27,"ports":{"S5":4,"S6":4}}]}
