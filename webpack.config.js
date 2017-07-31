const path = require('path')
const webpack = require('webpack')

module.exports = {
    entry: [
        './src/index.js'
    ],
    output: {
        filename: 'bundle.js',
        path: path.resolve('./deploy/MovieMarathon/')
    },

    // Enable sourcemaps for debugging webpack's output.
    devtool: 'cheap-module-eval-source-map',

    resolve: {
        // Add '.ts' and '.tsx' as resolvable extensions.
        extensions: ['.tsx', '.ts', '.js', '.scss', '.json']
    },

    module: {
        rules: [{
            test: /\.js$/,
            exclude: /node_modules/,
            loader: 'babel-loader'
        }, {
            test: /\.scss$/,
            loader: 'style-loader!css-loader?sourceMap&modules&camelCase!sass-loader?sourceMap'
        }, {
            test: /\.css$/,
            loader: "style-loader!css-loader?importLoaders=1"
        }, {
            test: /\.(png|woff|woff2|eot|ttf|svg)$/,
            loader: 'url-loader?limit=100000'
        }]
    },

    node: {
        fs: "empty"
    }
}