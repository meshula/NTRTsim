/*
 * Copyright © 2012, United States Government, as represented by the
 * Administrator of the National Aeronautics and Space Administration.
 * All rights reserved.
 * 
 * The NASA Tensegrity Robotics Toolkit (NTRT) v1 platform is licensed
 * under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 * http://www.apache.org/licenses/LICENSE-2.0.
 * 
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
 * either express or implied. See the License for the specific language
 * governing permissions and limitations under the License.
*/

#ifndef TG_MODEL_VISITOR_TGDLR_H
#define TG_MODEL_VISITOR_TGDLR_H

/**
 * @file tgModelVisitor.h
 * @brief Contains the definition of interface class tgModelVisitor_tgDLR
 * @author Brian Tietz and Drew Sabelhaus
 * $Id$
 */

// Forward declarations
//class tgLinearString;
class tgModel;
//class tgRod;

/**
 * Interface for ModelVisitor.
 */
class tgModelVisitor_tgDLR {
    
public:

  /** Virtual base classes must have a virtual destructor. */
  virtual ~tgModelVisitor_tgDLR() { }
 
  /**
   * Render a tgModel_tgDLR.
   * @param[in] model a const reference to a tgModel to render.
   */
  virtual void render(const tgModel& m) const {}

};

#endif