const path = require('path');
const webpack = require('webpack');

const defaultConfig = require('./webpack.config');
defaultConfig.devtool = 'source-map';
defaultConfig.output.filename = 'bundle.js';
defaultConfig.output.path = path.resolve('./docs/');
defaultConfig.plugins = defaultConfig.plugins || [];
defaultConfig.plugins.push(
    new webpack.optimize.UglifyJsPlugin({
        sourceMap: true
    }),
    new webpack.DefinePlugin({
        'process.env.NODE_ENV': JSON.stringify('production')
    })
);

module.exports = defaultConfig;