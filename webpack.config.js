const path = require('path');
const webpack = require('webpack');

module.exports = {
    entry: [
        './src/index.tsx'
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
            // All files with a '.ts' or '.tsx' extension will be handled by 'awesome-typescript-loader'.
            test: /\.tsx?$/,
            loader: 'awesome-typescript-loader'
        }, {
            // All output '.js' files will have any sourcemaps re-processed by 'source-map-loader'.
            enforce: 'pre',
            test: /\.js$/,
            loader: 'source-map-loader'
        }, {
            test: /\.scss$/,
            use: [{
                loader: 'style-loader'
            }, {
                loader: 'typings-for-css-modules-loader',
                options: {
                    camelCase: true,
                    modules: true,
                    namedExport: true,
                    sourceMap: true
                }
            }, {
                loader: 'sass-loader',
                options: {
                    sourceMap: true
                }
            }]
        },{
            test: /\.css$/,
            loader: "style-loader!css-loader?importLoaders=1"
        }, {
            test: /\.(png|woff|woff2|eot|ttf|svg)$/,
            loader: 'url-loader?limit=100000'
        }]
    }
};